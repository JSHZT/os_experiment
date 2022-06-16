class Memory(object):
    def __init__(self, maxsize):
        # self.minsize = minsize
        self.maxsize = maxsize
        self.plist = []
        
class partion(object):
    def __init__(self, start, end, minsize = 0, state = 0, id = 0):
        self.id = id
        self.start = start
        self.end = end
        self.size = self.end - self.start - minsize + 1
        self.state = state
        
    def update_size(self):
        self.size = self.end - self.start + 1

