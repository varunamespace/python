class SinglyLinkedList:
    class Node:
        def __init__(self,element,next):
            self.element = element
            self.next = next
    def __init__(self):
        self.head = None
        self.size = 0

    def is_Empty(self):
        return self.size == 0

    def __len__(self):
        return self.size


    def insert_node(self,e):
        element = self.Node(e,self.head)
        self.head = element
        self.size += 1

    def printLinkedList(self,head):
        data = self.head
        while data is None:
            print(data)
            data = self.head.next

    def remove_node(self):
        element = self.head.element
        self.head = self.head.next
        self.head = None
        return element




l = SinglyLinkedList()
l.insert_node(1)
l.insert_node(2)
l.insert_node(7)
print(l.__len__())
print(l.remove_node())
print(l.remove_node())

print(l.__len__())
