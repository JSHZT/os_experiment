from Page import *

def get_ad(inst_ad, size=10):
    page_id, inpage_ad = inst_ad// size, inst_ad % size
    return page_id, inpage_ad
    
def OPT(work, Virtual_Memory, allocated_memory):
    count_q = 0
    for i in range(len(work)):
        # print("当前分配的物理块中的页是  ", allocated_memory.pages_rec)
        page_id, inpage_ad = get_ad(work[i])
        # print("当前执行指令%d,所在页面是%d"%(work[i], page_id))
        if page_id in allocated_memory.pages_rec:
            # print("页面无需置换")
            continue
        else:
            if len(allocated_memory.pages) < allocated_memory.size:
                allocated_memory.pages.append(Virtual_Memory.pages[page_id])
                allocated_memory.pages_rec.append(page_id)
                # print("缺页中断，调入页面")
            else:
                temp = work[i:]
                max_ = 0
                for j in range(allocated_memory.size):
                    if allocated_memory.pages_rec[j] in temp:
                        now = temp.index(allocated_memory.pages_rec[j])
                    else:
                        rep_id = allocated_memory.pages_rec[j]
                        break
                    if now > max_:
                        max_ = now
                        rep_id = temp[max_]
                max_ = 0
                # print("缺页中断，页面%d被置换"%(rep_id))
                count_q += 1
                allocated_memory.pages_rec[allocated_memory.pages_rec.index(rep_id)] = page_id
                for k in range(allocated_memory.size):
                    if allocated_memory.pages[k].id == rep_id:
                        allocated_memory.pages[k] = Virtual_Memory.pages[page_id]
    print("缺页次数为:  ", count_q)
    res = (count_q + allocated_memory.size)/320 #缺页率
    print("缺页率为:  ", res)
    return

def LRU(work, Virtual_Memory, allocated_memory):
    count_q = 0
    for i in range(len(work)):
        # print("当前分配的物理块中的页是  ", allocated_memory.pages_rec)
        page_id, inpage_ad = get_ad(work[i])
        # print("当前执行指令%d,所在页面是%d"%(work[i], page_id))
        if page_id in allocated_memory.pages_rec:
            # print("页面无需置换")
            continue
        else:
            if len(allocated_memory.pages) < allocated_memory.size:
                allocated_memory.pages.append(Virtual_Memory.pages[page_id])
                allocated_memory.pages_rec.append(page_id)
                # print("缺页中断，调入页面")
            else:
                temp = work[:i]
                temp.reverse()
                max_ = 0
                for j in range(allocated_memory.size):
                    if allocated_memory.pages_rec[j] in temp:
                        now = temp.index(allocated_memory.pages_rec[j])
                    else:
                        rep_id = allocated_memory.pages_rec[j]
                        break
                    if now > max_:
                        max_ = now
                        rep_id = temp[max_]
                max_ = 0
                # print("缺页中断，页面%d被置换"%(rep_id))        
                count_q += 1        
                allocated_memory.pages_rec[allocated_memory.pages_rec.index(rep_id)] = page_id
                for k in range(allocated_memory.size):
                    if allocated_memory.pages[k].id == rep_id:
                        allocated_memory.pages[k] = Virtual_Memory.pages[page_id]
    print("缺页次数为:  ", count_q)
    res = (count_q + allocated_memory.size)/320 #缺页率
    print("缺页率为:  ", res)
    return
    

def init_page(memory):
    start = 0
    for i in range(memory.size): 
        page = pages(i)
        page.instructions, start = list(range(start, start+10)), start + 10
        memory.pages.append(page)
        memory.pages_rec.append(i)
        
if __name__ == "__main__":
    while 1:
        try:
            work = get_work()
            break
        except:
            pass
    page_plan = []
    print("页面引用串为：")
    for i in range(len(work)):
        page_id, inpage_ad = get_ad(work[i])
        page_plan.append(page_id)
    print(page_plan)
    Virtual_Memory = Memory(32)
    allocated_memory = Memory(3)
    init_page(Virtual_Memory)
    # print("OPT算法：")
    # OPT(work, Virtual_Memory, allocated_memory)
    print("LRU算法：")
    LRU(work, Virtual_Memory, allocated_memory)

    