class Node:
    def __init__(self,val):
        self.next = None
        self.prev = None
        self.data = val
class doubleLinked:
    def __init__(self):
        self.head = None

    def createlist(self,list):
        start = self.head
        n = len(list)
        temp = start
        i = 0
        while i<n:
            newNode = Node(list[i])
            if i ==0:
                start = newNode
                temp = start
            else:
                temp.next = newNode
                newNode.prev = temp
                temp = temp.next
            i = i + 1
        self.head = start
        return start

    def printlist(self):
        temp = self.head
        r = ""
        while temp!=None:
            r = r + (str(temp.data) + "=>")
            temp = temp.next
        print(r)

    def countnode(self):
        temp = self.head
        count = 0
        while(temp!=None):
            temp = temp.next
            count = count + 1
        return count

    def insertnode(self,val,pos):
        temp = self.head
        n = self.countnode()
        newNode = Node(val)
        if(pos==0):
            newNode.next = temp
            temp.prev = newNode
            self.head = newNode
            return self.head
        if(pos==n+1):
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next - newNode
            newNode.prev = temp.next
            return self.head
        i = 1
        while(i<pos):
            temp = temp.next
            i = i + 1
        afternode = temp.next
        newNode.next = afternode
        afternode.prev = newNode
        temp.next = newNode
        newNode.prev = temp
        return self.head
    def deletenode(self,pos):
        temp = self.head
        count = self.countnode()
        if pos>count:
            return temp
        elif pos == 1:
            tar = temp.next
            tar.prev = temp
            self.head = tar
        elif pos==count:
            while temp.next is not None:
                temp = temp.next
            tar = temp.prev
            temp.prev = None
            tar.next = None
        else:
            c = 1
            while temp.next!=None and c<pos:
                temp = temp.next
                c = c + 1
            pre = temp.prev
            ne = temp.next
            pre.next = ne
            ne.prev = pre
        return self.head

new = doubleLinked()
a = [5,4,2,1]
new.createlist(a)
#new.printlist()
new.printlist()
new.deletenode(3)
new.printlist()
new.deletenode(2)
new.printlist()
new.deletenode(1)
new.printlist()
