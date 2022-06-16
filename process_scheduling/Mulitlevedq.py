from PCB import Queue, PCB
from operator import attrgetter

def init_PcbPlan(nums):
    G.pcb_plan = []
    G.maxtime = 0
    for i in range(nums):
        pcb_item = {}
        pcb_item["name"] = str(input("请输入第{}个进程的名字::".format(i+1)))
        pcb_item["arrive_time"] = int(input("请输入第{}个进程的到达时间::".format(i+1)))
        temp = pcb_item["need_time"] = int(input("请输入第{}个进程的需要时间::".format(i+1)))
        G.pcb_plan.append(PCB(pcb_item))
        G.maxtime, temp = G.maxtime + temp, 0
        print('')
    G.pcb_plan.sort(key=attrgetter('arrive_time'))
    return 

def update(curtime, mfq):                    
    while G.pcb_plan and G.pcb_plan[0].arrive_time == curtime:
        mfq.queue_list[0].push(G.pcb_plan.pop(0))   
        
def get_que(level):
    que_list = []
    to_que = []
    for i in range(level):
        que_list.append(Queue(i, []))
        to_que.append(Queue(i, []))
    return que_list, to_que

class MulitlevedFeedbackQueue():
    def __init__(self, queue_list, to_que, q_first, maxtime):
        self.queue_list=queue_list
        self.to_que = to_que
        self.q_first=q_first
        self.maxtime=maxtime
        
    def scheduling(self):
        process = []
        q_first=self.q_first
        curtime = 0
        for i in range(len(self.queue_list)):
            if i==0:
                self.queue_list[i].q = q_first
                self.queue_list[i].q_cp=self.queue_list[i].q
            else :
                self.queue_list[i].q=self.queue_list[i-1].q*2
                self.queue_list[i].q_cp = self.queue_list[i].q
                
        while curtime < self.maxtime:
            print("当前是第%d时刻"%(curtime))
            update(curtime, self)
            curtime += 1
            for i in range(len(self.queue_list)):
                currentQueue=self.queue_list[i]
                if currentQueue.process_list:
                    if currentQueue.get(0).left_serve_time > 0:
                        currentQueue.get(0).left_serve_time -= 1
                        currentQueue.get(0).run_time += 1
                        currentQueue.q_cp -= 1
                        print('第%d队列 当前执行进程 %s'%(i, currentQueue.get(0).name))
                    if currentQueue.get(0).left_serve_time <= 0:
                        print('服务完成并弹出:',currentQueue.get(0).name)
                        currentQueue.get(0).left_serve_time=0
                        currentQueue.get(0).end_time = curtime - 1
                        currentQueue.get(0).update_turn_time()
                        process.append((currentQueue.get(0).name, currentQueue.get(0).arrive_time, currentQueue.get(0).need_time, currentQueue.get(0).run_time, currentQueue.get(0).end_time, currentQueue.get(0).turn_time, currentQueue.get(0).turn_time_E))
                        currentQueue.delete(0)
                        continue
                    if currentQueue.q_cp <= 0 :
                        if currentQueue.get(0).left_serve_time > 0:
                            print('进程 %s 在 第%d队列 没有执行完毕,需要添加至下一队列末尾'%(currentQueue.get(0).name, i))
                            if i == len(self.queue_list)-1:
                                self.queue_list[i].push(currentQueue.get(0))
                            else:
                                self.to_que[i+1].push(currentQueue.get(0))
                        currentQueue.q_cp = currentQueue.q
                        currentQueue.delete(0)
                        continue
                    
                else:
                    print("'第%d队列 没有进程执行"%(i))
            for i in range(1, len(self.queue_list)):
                if to_que[i].process_list:
                    self.queue_list[i].push(self.to_que[i].get(0))
                    self.to_que[i].delete(0)
        print("进程        到达时间        服务时间        完成时间        周转时间        带权周转时间")
        temp_ = 0
        for i in process:
            temp_ += i[6]
            print("%c\t\t%d\t\t%d\t\t%d\t\t%.2f\t\t%.2f\n"%(i[0], i[1], i[3], i[4], i[5], i[6]) )
        print("平均带权周转时间为：", temp_/len(process))

   
if __name__=='__main__':
    class G:
        pcb_plan = []
        maxtime = 0
    pcb_nums = int(input("请输入进程数"))
    init_PcbPlan(pcb_nums)
    level = 6
    queue_list, to_que=get_que(level)
    mfq=MulitlevedFeedbackQueue(queue_list, to_que, 1, G.maxtime)
    mfq.scheduling()