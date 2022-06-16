import random
class file(object):
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size
        self.block_list = []
    
    def show_block(self)->None:
        print(self.block_list)

class disk(object):
    def __init__(self, block_size = 4, cylinder_nums=2000, surface_nums=8, sector_nums=4) -> None:
        self.cylinder_nums = cylinder_nums
        self.surface_nums = surface_nums
        self.sector_nums = sector_nums
        self.block_size = block_size
        self.map = [[random.randint(0, 1) for _ in range(self.surface_nums*self.sector_nums)] for _ in range(self.cylinder_nums)]
        self.file_list = []
        
    def get_block(self, i, j)->int:
        return self.surface_nums * self.sector_nums * i + j + 1
    
    def find_empty(self):
        for i in range(self.cylinder_nums):
            for j in range(self.surface_nums*self.sector_nums):
                if self.map[i][j] == 0:
                    return i, j
        return -1, -1
    
    def find_file(self, name):
        for i in range(len(self.file_list)):
            if name == self.file_list[i].name:
                return i
        return None
        
    def Allocation(self, file_)->list:
        mapcp = self.map.copy()
        size = file_.size
        process = []
        while size > 0:
            size -= self.block_size
            i, j = self.find_empty()
            if i == -1: 
                self.map = mapcp
                return []
            self.map[i][j] = 1
            process.append([self.get_block(i, j), i, j])
        for item in process:
            self.map[item[1]][item[2]] = 1
            file_.block_list.append(item[0])
        self.file_list.append(file_)
        return process
    
    def al_s_b(self, i, j):
        self.map[i-1][j-1] = 0
        return 
    
    def get_ij(self, b):
        i = int((b - 1) / (self.surface_nums * self.sector_nums))
        j = int((b - 1) % (self.surface_nums * self.sector_nums))
        return i, j
    
    def rec_s_b(self, i, j):
        self.map[i-1][j-1] = 1
        return 
    
    def Recycle(self, file_name)->None:
        res = self.find_file(file_name)
        if res is None:
            return
        file_ =  self.file_list[res]
        for block in file_.block_list:
            i = int((block - 1) / (self.surface_nums * self.sector_nums))
            j = int((block - 1) % (self.surface_nums * self.sector_nums))
            if i >= 0 and i < len(self.map) and j >= 0 and j < len(self.map[0]):
                self.map[i][j] = 0
        self.file_list.pop(res)
        
    
    def show_map(self)->None:
        for i in range(32):
            print(str(i)+" ", end="")
        print("")
            
        for i in range(len(self.map)):
            if i == (1873):
                print(str(i)+" ", end="")
                for j in range(len(self.map[0])):
                    print(str(self.map[i][j])+" ", end="")
                print("")
        
if __name__ == "__main__":
    disk1 = disk()
    # file_ = file('A', 9)
    # disk1.show_map()
    disk1.al_s_b(1599, 17)
    disk1.show_map()
    i, j = disk1.get_ij(59999)
    disk1.rec_s_b(i, j)
    disk1.show_map()