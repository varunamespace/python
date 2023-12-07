
class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, next, prev):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = None

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert__between(self,e,pred,succ):
        newest = self._Node(e,pred,succ)
        pred._next = newest
        succ._prev = newest
        self._size += 1
        return newest

    def _delete_node(self,node):
        node._prev = pred
        node._next = succ
        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element
        node._prev = node._next = element = None
        return element

    class LinkedDeque(_DoublyLinkedBase):
        def first(self):
            if self.is_empty():
                raise NameError("deque is empty")
            return self._header._next._element

        def last(self):
            return self._trailer._prev._element

        def insert_first(self, e):
            return self._insert__between(e, self._header, self._header._next)

        def insert_last(self, e):
            return self._insert__between(e, self._trailer._prev, self._trailer)

        def delete_first(self):
            return self._delete_node(self._header._next)

        def delete_last(self):
            return self._delete_node(self._trailer._prev)


class LinkedDeque(_DoublyLinkedBase):
    def first(self):
        if self.is_empty():
            raise NameError("deque is empty")
        return self._header._next._element

    def last(self):
        return self._trailer._prev._element

    def insert_first(self,e):
        return self._insert__between(e,self._header,self._header._next)

    def insert_last(self,e):
        return self._insert__between(e,self._trailer._prev,self._trailer)

    def delete_first(self):
        return self._delete_node(self._header._next)

    def delete_last(self):
        return self._delete_node(self._trailer._prev)




