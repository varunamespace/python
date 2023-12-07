class Queue:
    def __init__(self):
        self.q = []
        self.size = 0
    def enqueue(self,val):
        self.q.insert(0,val)
        size = size + 1
    def dequeue(self):
        self.q.pop(-1)
        size = size - 1
    def peek(self):
        return self.q[-1]
    def isEmpty(self):
        if self.size ==0:
            return  True
        else:
            return False
    def 



