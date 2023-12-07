class Node:
    def __init__(self,val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        res = ""
        while temp:
            res = res + (str(temp.data) + " ")
            temp = temp.next
        print(res)

    def add(self,val,ind):
        if ind == 0:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
            return
        def findprev(ind):
            find = self.head
            count = 1
            while(count<ind):
                find = find.next
                count = count + 1
            return find
        previous = findprev(ind)
        nextnode = previous.next
        toinsert = Node(val)
        toinsert.next = nextnode
        previous.next = toinsert

    def delenode(self,key):
        temp = self.head
        if temp is None:
            return
        if(temp.data == key):
            self.head = temp.next
            temp = None
            return
        while(temp.next.data!=key):
            temp = temp.next
        todel = temp.next
        temp.next = todel.next
        todel.next = None


linked = LinkedList()
"""node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(3)"""
node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
linked.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
#node4.next = node2
#linked.printList()

t = node1
r = node1
while t and r:
    t = t.next
    r = r.next.next
    if r==t:
        print(1)
        break
print(2)
"""temp = node1
while temp and temp.next:
    if temp.data==temp.next.data and temp.next:
        nextdata = temp.next
        if nextdata.next is None:
            temp.next = None
            break
        while temp.data==nextdata.data and nextdata.next:
            nextdata = nextdata.next
        temp.next = nextdata
    else:
        temp = temp.next
"""

#1,1,2,3,3