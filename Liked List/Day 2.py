####################Remove nth node from the last of the list#####################
class Link:
    def __init__(self,val):
        self.data = val
        self.next = None

l1 = Link(1)
l2 = Link(2)
l3 = Link(3)
l4 = Link(4)
l5 = Link(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

"""
class Solution(object):
    def deleteDuplicates(self, head):
        temp = head
        while (temp and temp.next):
            if (temp.next.val == temp.val):
                temp.next = temp.next.next
                continue
            temp = temp.next
        return head

"""


