class CircularQueue:
    class Node:
        def __init__(self,element,next):
            self.element = element
            self.next = None

    def __init__(self):
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def first(self):
        if self.isEmpty():
            return NameError("its empty")
        first = self.tail.next
        return first.element

    def dequeue(self):
        if self.isEmpty():
            return NameError("its empty")
        oldhead = self.tail.next
        if self.size == 1:
            self.tail = None
        self.tail.next = oldhead.next
        self.size = self.size - 1
        return oldhead.element

    def enqueue(self,e):
        newest = self.Node(e,None)
        if self.isEmpty():
            newest.next = newest
        else:
            newest.next = self.tail.next
            self.tail.next = newest
        self.tail = newest
        self.size += 1

    def rotate(self):
        if self.size > 0:
            self.tail = self.tail.next







