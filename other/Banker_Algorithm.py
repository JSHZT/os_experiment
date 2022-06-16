import numpy as np

def bank(dict):
    p_id, Request = dict['Request'][0], dict['Request'][1]
    Need = dict['Need']
    Available = dict['Available']
    Allocation = dict['Allocation'] 
    n = Allocation.shape[0]
    
    if not (Request <= Need[p_id]).all():
        exit(0)
    if not (Request <= Available[p_id]).all():
        return False, []

    # copy
    AvailableCp = np.copy(Available)
    AllocationCp = np.copy(Allocation)
    NeedCp = np.copy(Need)

    Available = Available - Request
    Allocation[p_id] = Allocation[p_id] + Request
    Need[p_id] = Need[p_id] - Request

    process = []

    Work = np.copy(Available)
    Finish = np.array([0, 0, 0, 0, 0], dtype=np.bool_)
    while True:
        has_found = False
        for i in range(n):
            if Finish[i] == False and (Need[i] <= Work).all():
                Work = Work + Allocation[i]
                Finish[i] = True
                has_found = True
                process.append(i)
        if not has_found:
            break
    status = Finish.all()
    if not status:
        Available = AvailableCp
        Allocation = AllocationCp
        Need = NeedCp
    return status, process

def init_(k = 0):
    dict = {}
    n = int(input("请输入进程数量："))
    m = int(input("请输入资源数量："))
    Max = []
    Allocation = []
    Request = []
    for i in range(n):
       Max.extend(list(map(int, input("请输入第%d进程的各种资源的最大需求量（不同类别资源用空格隔开）"%(i+1)).split())))
       Allocation.extend(list(map(int, input("请输入第%d进程的各种资源的已分配量（不同类别资源用空格隔开）"%(i+1)).split())))
    Available = list(map(int, input("请输入当前各种资源的可分配量（不同类别资源用空格隔开）").split()))
    if k == 1:
        p_id = int(input("请输入需要请求资源的进程id"))
        Request = list(map(int, input("请输入各种资源的请求量（不同类别资源用空格隔开）").split()))
    else:
        p_id = 1
        Request = [0, 0, 0]
    dict['Max'] = np.array(Max, dtype=np.int32).reshape(n, m) 
    dict['Allocation'] = np.array(Allocation, dtype=np.int32).reshape(n, m) 
    dict['Need'] = dict['Max'] - dict['Allocation']
    dict['Available'] = np.array(Available, dtype=np.int32)
    dict['Request'] = (p_id, np.array(Request, dtype=np.int32))
    return dict

if __name__ == '__main__':
    dict = init_()
    status, process = bank(dict)
    namee = {
        '0':'P1',
        '1':'P2',
        '2':'P3',
        '3':'P4',
        '4':'P5',
    }
    if status :
        print("具有安全序列如下：")
        for i in range(len(process)):
            if i == len(process)-1:
                print(namee[str(i)])
            else:
                print(namee[str(i)] + "->", end="")
    else:
        print("不安全")
    dict = init_(k=1)
    status, process = bank(dict)
    if status :
        print("具有安全序列：", process)
    else:
        print("不安全")