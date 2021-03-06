M = 4
N = 17

class page:
    def __init__(self,num,time):      
        self.num = num  
        self.time = time

class Solution:
    def __init__(self):
        self.b = [page(-1,M-i-1) for i in range(0,M)]
        self.c = [[-1 for i in range(0,N)] for j in range(0,M)]
        self.queue = []
        self.k = -1
        self.flag =-1
        # self.process()

    def print_string(self):
        print("|---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+---|")

    def get_max(self,b):
        max = -1
        flag = 0
        for i in range(0,M):
            if b[i].time >max:
                max = b[i].time
                flag = i
        return flag 

    def equation(self,fold,b):
        for i in range(0,M):
            if fold == b[i].num:
                return i
        return -1
    
    def opt(self, fold, b, index, a):
        max = -1
        val = self.equation(fold,b)
        if val >= 0:
            pass
        else:
            self.queue.append(fold)
            self.k += 1

            for j in range(0,M):
                for k in range(index+1,N):
                    if b[j].num==a[k]:
                        b[j].time = k-j
                    else:
                        b[j].time = 20

            for i in range(0, M):
                if b[i].num ==-1:
                    val = i
                    break;
                else:
                    if b[i].time > max:
                        max = b[i].time
                        val = i
            b[val].num = fold
    # LRU
    def lru(self, fold, b):
        val = self.equation(fold, b)
        if val >= 0:
            b[val].time = 0
            for i in range(0, M):
                if i != val:
                    b[i].time += 1
        else:
            self.queue.append(fold)
            self.k += 1
            val = self.get_max(b)
            b[val].num = fold
            b[val].time = 0
            for i in range(0, M):
                if (i != val):
                    b[i].time += 1

    def Myprint(self,a):
        self.print_string()
        for j in range(0, N):
            print("|%2d" % (a[j]), end=" ")
        print("|")
        self.print_string()
        for i in range(0, M):
            for j in range(0, N):
                if self.c[i][j] == -1:
                    print("|%2c" % (32), end=" ")
                else:
                    print("|%2d" % (self.c[i][j]), end=" ")
            print("|")
        self.print_string()
        print("???????????????")
        for i in range(0, self.k + 1):
            print("%2d" % (self.queue[i]), end=" ")
        print("\n??????????????????%6d\n????????????%16.6f" % (self.k + 1, (float)(self.k + 1) / N))


    def process(self, page_plan):
        a = page_plan

        for i in range(0, N):
            self.fifo(a[i], self.b)
            self.c[0][i] = a[i]

            for j in range(0, M):
                self.c[j][i] = self.b[j].num
        # ????????????
        print("fifo????????????????????????")
        self.Myprint(a)

        # ?????????????????????
        self.b = [page(-1, M - i - 1) for i in range(0, M)]
        # ???????????????????????????????????????
        self.c = [[-1 for i in range(0, N)] for j in range(0, M)]
        # ??????????????????
        self.queue = []
        self.k = -1
        for i in range(0, N):
            self.lru(a[i], self.b)
            self.c[0][i] = a[i]

            # ???????????????????????????????????????
            for j in range(0, M):
                self.c[j][i] = self.b[j].num
        # ????????????
        print("lru????????????????????????")
        self.Myprint(a)

        # opt ??????
        # ?????????????????????
        self.b = [page(-1, M - i - 1) for i in range(0, M)]
        # ???????????????????????????????????????
        self.c = [[-1 for i in range(0, N)] for j in range(0, M)]
        # ??????????????????
        self.queue = []
        self.k = -1
        for i in range(0, N):
            self.opt(a[i], self.b, i,a)
            self.c[0][i] = a[i]

            # ???????????????????????????????????????
            for j in range(0, M):
                self.c[j][i] = self.b[j].num

        # opt ????????????
        print("opt????????????????????????")
        self.Myprint(a)
if __name__ == "__main__":
    page_plan = [1,0,1,0,2,4,1,0,0,8,7,5,4,3,2,3,4]
    sol = Solution()
