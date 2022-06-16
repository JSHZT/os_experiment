from audioop import reverse
from operator import attrgetter
import PCB

def init_PcbPlan(nums):
    G.pcb_plan = []
    G.maxtime = 0
    for i in range(nums):
        pcb_item = {}
        pcb_item["name"] = str(input("请输入第{}个进程的名字::".format(i+1)))
        pcb_item["arrive_time"] = int(input("请输入第{}个进程的到达时间::".format(i+1)))
        temp = pcb_item["need_time"] = int(input("请输入第{}个进程的需要时间::".format(i+1)))
        G.pcb_plan.append(PCB.PCB(pcb_item))
        G.maxtime, temp = G.maxtime + temp, 0
        print('')
    G.pcb_plan.sort(key=attrgetter('arrive_time'))
    return 

def update_hp(curtime):
    while G.pcb_plan and G.pcb_plan[0].arrive_time == curtime:
            G.PCB_hp.append(G.pcb_plan.pop(0))
    G.PCB_hp.sort(key=attrgetter('RRN'), reverse=True)

def update_RNN_():
    for pcb in G.PCB_hp:
        pcb.waiting_time += 1
        pcb.update_RNN()
        
def run():
    curpcb = None
    curtime = starttime = 0
    pcb_list =[]
    print("当前时间        当前运行进程\n")
    
    while curtime <= G.maxtime:
        update_hp(curtime)
        if curpcb is None:
            try:
                curpcb = G.PCB_hp.pop(0)
                curpcb.start_time = curtime
                G.PCB_hp.sort(key=attrgetter('RNN'), reverse=True)
            except:
                if G.pcb_plan == []:
                    return
        print("%d\t\t%c"%(curtime, curpcb.name) )
        
        if curpcb is not None and curpcb.need_time == 0:
            curpcb.end_time = curtime - 1
            curpcb.run_time = curtime - starttime
            curpcb.turn_time = curtime - curpcb.arrive_time
            curpcb.turn_time_E = curpcb.turn_time / curpcb.run_time
            starttime = curtime
            pcb_list.append(curpcb)
            try:
                curpcb = G.PCB_hp.pop(0)
                G.PCB_hp.sort(key=attrgetter('RRN'), reverse=True)
            except:
                pass
        update_RNN_()
        G.PCB_hp.sort(key=attrgetter('RRN'), reverse=True)
        if curpcb is not None:
            curpcb.need_time -= 1
        curtime += 1
    pcb_list.sort(key=attrgetter('arrive_time'))
    print("进程        到达时间        服务时间        完成时间        周转时间        带权周转时间")
    sums = 0
    for i in (pcb_list):
        print("%c\t\t%d\t\t%d\t\t%d\t\t%.2f\t\t%.2f\n"%(i.name, i.arrive_time, i.run_time, i.end_time, i.turn_time, i.turn_time_E) )
        sums += i.turn_time_E
    print("平均带权周转时间\t"+"%.2f"%(sums/len(pcb_list)))
    return

if __name__ == "__main__":
    class G:
        PCB_hp = []
        pcb_plan = []
        maxtime = 0
    pcb_nums = int(input("请输入进程数"))
    init_PcbPlan(pcb_nums)
    run()
    