from memory import Memory, partion
from operator import attrgetter

def show_memory(merory):
    print("分配状态    分区号    起始地址   终止地址  分区大小")
    for i in range(len(memory.plist)):
        p = memory.plist[i]
        if p.state == 0:
            print("%s%s%s%11.d%11.d%10.d"%('空闲',"          ", p.id,  p.start, p.end, p.size))
        else:
            print("%s%s%s%11.d%11.d%10.d"%('已分配',"        ", p.id,  p.start, p.end, p.size))

def has_find_work(memory, work_id):
    for j in range(len(memory.plist)):
        if memory.plist[j].id == work_id:
            return True
    return False

def best_fit(memory, work_id, work_size):
    if has_find_work(memory, work_id):
        print("作业已存在\n")
        return False
    que = memory.plist.copy()
    que.sort(key=attrgetter("state", "size"))
    is_more = -1
    is_fit = -1
    for i in range(len(que)):
        p = que[i]
        if p.state == 0 and p.size > work_size:
            is_more = p.start
            break
        elif p.state == 0 and p.size == work_size:
            is_fit = p.start
            break
    if is_more == -1 and is_fit == -1:
        print("内存空间不足\n")
        return False
    for i in range(0, len(memory.plist)):
        p = memory.plist[i]
        if p.start == is_more:
            remaining = partion(p.start + work_size, p.end, id = p.id) 
            has_distribute = partion(p.start, p.start + work_size - 1, state=1, id = work_id)
            del memory.plist[i]
            memory.plist.insert(i, remaining)
            memory.plist.insert(i, has_distribute)
            show_memory(memory.plist)
            return True
        elif p.start == is_fit:
            p.state = 1
            show_memory(memory.plist)
            return True

def deal(memory, work):
    work_id, work_op, work_size = work[0], work[1], work[2]
    if work_op == 1:
        print("进程"+str(work_id)+"申请"+str(work_size)+"KB")
        if has_find_work(memory, work_id):
            print("作业已存在\n")
            return False
        if best_fit(memory, work_id, work_size):
            return True
        return False
    elif work_op == 0:
        if not has_find_work(memory, work_id):
            print("作业不存在\n")
            return False
        print("进程"+str(work_id)+"释放"+str(work_size)+"KB")
        free(memory, work_id)
        return True
    
def free(memory, work_id):
    target = 0
    for i in range(len(memory.plist)):
        p = memory.plist[i]
        if p.id == work_id:
            p.state = 0
            target = i
            p.id=0
            break
    if target - 1 > 0:
        if memory.plist[target - 1].state == 0:
            a = partion(memory.plist[target - 1].start, memory.plist[target].end)
            del memory.plist[target - 1]
            del memory.plist[target - 1]
            memory.plist.insert(target - 1, a)
            target = target - 1
    if target + 1 < len(memory.plist):
        if memory.plist[target + 1].state == 0:
            a = partion(memory.plist[target].start, memory.plist[target + 1].end)
            del memory.plist[target]
            del memory.plist[target]
            memory.plist.insert(target, a)
    show_memory(memory.plist)

def init_work_list(memory):
    # nums = int(input("请输入要分配内存的作业数量：：："))
    # for i in range(nums):
    plist = [
        (1, 1, 100), 
        (2, 1, 150), 
        (3, 1, 300),
        (2, 0, 150),
        (4, 1, 80),
        (3, 0, 300)
    ]
    for i in plist:
        deal(memory, i)

if __name__ == "__main__":
    maxsize = int(input("请输入存储器内存大小：：："))
    # minsize = int(input("请输入允许存储器最小碎片大小：：："))
    # memory = Memory(maxsize, minsize)
    memory = Memory(maxsize)
    part0 = partion(0, maxsize-1)
    memory.plist.append(part0)
    init_work_list(memory)