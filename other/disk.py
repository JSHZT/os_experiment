class disk(object):
    def __init__(self, cylinder_nums, surface_nums, sector_nums) -> None:
        self.cylinder_nums = cylinder_nums
        self.surface_nums = surface_nums
        self.sector_nums = sector_nums

def SSTF(start, work_plan):
    print("使用SSTF磁盘调度算法")
    print("当前调度请求序列为：", work_plan)
    print("当前初始轨道为：", start) 
    lens = len(work_plan)
    count = 0
    list_2 = []
    process = []
    while len(work_plan) != 0:
        for i in work_plan:
            list_2.append(abs(start - i))
        tidy = min(list_2)
        count += tidy
        pn = list_2.index(tidy)
        start = work_plan[pn]
        process.append(start)
        work_plan.pop(pn)
        list_2.clear()
    print("总共移动了  %d  个磁道"%(count))
    print("调度顺序为：", process)
    print("平均寻道长度：", count/lens)
    
    
def SCAN(start, work_plan):
    print("使用SCAN磁盘调度算法")
    print("当前调度请求序列为：", work_plan)
    print("当前初始轨道为：", start) 
    print("当前初始方向是向右移动：") 
    lens = len(work_plan)
    count = 0
    process = []
    planCP = work_plan.copy()
    planCP.sort()
    for i in planCP:
        if start <= i:
            pn = planCP.index(i)
            break
    for j in range(pn, len(planCP)):
        count += abs(start - planCP[j])
        start = planCP[j]
        process.append(start)
    while pn > 0:
        pn -= 1
        count += start - planCP[pn]
        start = planCP[pn]
        process.append(start)
        
    print("总共移动了  %d  个磁道"%(count))
    print("调度顺序为：", process)
    print("平均寻道长度：", count/lens)
    return

def CSCAN(start, work_plan):
    print("使用CSCAN磁盘调度算法")
    print("当前调度请求序列为：", work_plan)
    print("当前初始轨道为：", start) 
    print("当前初始方向是向右移动：") 
    
    count = 0
    process = []
    planCP = work_plan.copy()
    planCP.sort()
    temp = 0
    for i in planCP:
        if start <= i:
            temp = pn = planCP.index(i)
            break
    for j in range(pn, len(planCP)):
        count += abs(start - planCP[j])
        start = planCP[j]
        process.append(start)
    start = 0
    for j in range(start, temp):
        count += abs(start - planCP[j])
        start = planCP[j]
        process.append(start)

        
    print("总共移动了  %d  个磁道"%(count))
    print("调度顺序为：", process)
    return

if __name__ == "__main__":
    work_plan = [23, 376, 205, 132, 19, 61, 190, 398, 29, 4, 18, 40]
    start = 100
    SSTF(start, work_plan)
    