#1.Combining the two sorted array
"""
class Link:
    def __init__(self,val):
        self.data = val
        self.next = None
def sorttwo(l1,l2):
    temp = Link(0)
    ans = temp
    while l1 and l2:
        if l1.data>l2.data:
            temp.next = l2
            l2 = l2.next
        else:
            temp.next = l1
            l1 = l1.next
        temp = temp.next

    while l1:
        temp.next = l1
        l1 = l1.next
        temp = temp.next
    while l2:
        temp.next = l2
        l2 = l2.next
        temp = temp.next

    return ans.next
l11 = Link(1)
l12 = Link(2)
l13 = Link(4)
l11.next = l12
l12.next = l13

l21 = Link(1)
l22 = Link(3)
l23 = Link(4)
l21.next = l22
l22.next = l23
ans = sorttwo(l11,l21)
print(ans)
while ans.next is not None:
    print(str(ans.data))
    ans = ans.next
"""
"""
#Cycle Linked list
class Link:
    def __init__(self,val):
        self.data = val
        self.next = None

def rabbitandturtle(a):
    r = l1
    t = l1
    while r and t:
        r = r.next.next
        t = t.next
        if t==r:
            return ("true")
    else:
        return("false")

l1 = Link(1)
l2 = Link(2)
l3 = Link(3)
l4 = Link(4)
l5 = Link(5)
l6 = Link(11)
l7 = Link(6)
l8 = Link(8)
l9 = Link(9)
l10 = Link(7)
l11 = Link(3)
#//////////////////////////
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7
l7.next = l8
l8.next = l9
l9.next = l10
l10.next = l3
print(rabbitandturtle(l1))
"""
class Link:
    def __init__(self,val):
        self.data = val
        self.next = None

l1= Link(1)
l2= Link(2)
l3= Link(3)
l4= Link(4)
l5= Link(5)
l1.next=(l2)
l2.next=(l3)
l3.next=(l4)
l4.next=(l5)


def rever(l):
    temp = None
    while l is not None:
        ne = l.next
        l.next = temp
        temp = l
        l = ne
    return temp

rever(l1)


