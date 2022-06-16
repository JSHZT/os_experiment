class PCB:
    def __init__(self, dict):
        self.arrive_time = dict["arrive_time"]
        self.need_time = dict["need_time"]
        self.left_serve_time = dict["need_time"]
        self.name = dict["name"]
        self.run_time = 0
        self.end_time = 0
        self.turn_time = 0
        self.turn_time_E = 0
        self.waiting_time = 0
        self.start_time = 0
        self.RRN = (0 + self.need_time) / self.need_time
        
    def update_RNN(self):
        self.RRN = (self.waiting_time + self.need_time) / self.need_time
        return
    
    def update_turn_time(self):
        self.turn_time = self.end_time - self.arrive_time + 1
        self.turn_time_E = self.turn_time / self.run_time
    
class Queue(object):
    def __init__(self,level,process_list):
        self.level=level
        self.process_list=process_list
        self.q=0
        self.q_cp=0

    def size(self):
        return len(self.process_list)

    def get(self,index):
        return self.process_list[index]    

    def push(self,process):
        self.process_list.append(process)
        
    def pop(self):
        self.process_list.pop(0)

    def delete(self,index):
        self.process_list.remove(self.process_list[index])
        


