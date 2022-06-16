import random

class pages(object):
    def __init__(self,id):      
        self.id = id  
        self.instructions = []
    
class Memory(object):
    def __init__(self, size=3):
        self.size = size
        self.pages = []
        self.pages_rec = []
        
def get_work(work_len=320):
    def push_inst_to_work(id, work, has_get):
        work.append(id)
        has_get += 1   
        return has_get
    has_get = 0
    work = []
    while has_get < work_len:
        m = random.randint(0, 319)
        has_get = push_inst_to_work(m, work, has_get)
        has_get = push_inst_to_work(m+1, work, has_get)
        m1 = random.randint(0, m-1)
        while m1 < 0 or m1 >= 317:
            m1 = random.randint(0, m-1)
        has_get = push_inst_to_work(m1, work, has_get)
        has_get = push_inst_to_work(m1+1, work, has_get)
        m2 = random.randint(m1+2, 319)
        while m2 > 318:
            m2 = random.randint(m1+2, 319)
        has_get = push_inst_to_work(m2, work, has_get)
        has_get = push_inst_to_work(m2+1, work, has_get)
    return work[0:320]

if __name__ == "__main__":
    while 1:
        try:
            work = get_work()
            break
        except:
            pass
    
    print(len(work))