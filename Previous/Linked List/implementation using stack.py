class LinkedList:
    class Node:
        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def push(self,element):
        self.head = self.Node(element,self.head)
        self.size += 1

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self.head

    def pop(self):
        if self.is_empty():
            raise NameError("stack is empty")
        ans = self.head.element
        self.head = self.head.next
        self.size -= 1
        return ans

    def printlist(self):
        return self.head.element


l = LinkedList()
l.push(1)
l.top()
print(l.top())








