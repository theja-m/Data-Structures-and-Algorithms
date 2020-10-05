class CircularLinkedList:
    class _Node:
        __slots__ = '_data', '_next'


        def __init__(self, value, next):
            self._data = value
            self._next = next


    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0


    def is_empty(self):
        return self._size == 0


    def add_first(self, value):
        new_node = self._Node(value, None)
        if self.is_empty():
            new_node._next = new_node
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._tail._next = new_node
        self._head = new_node
        self._size += 1


    def add_last(self, value):
        new_node = self._Node(value, None)
        if self.is_empty():
            new_node._next = new_node
            self._head = new_node
            self._tail = new_node
        else:
            new_node._next = self._head
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1


    def add_particular(self, value, position):
        new_node = self._Node(value, None)
        i = 1
        temp = self._head
        while i < position-1:
            temp = temp._next
            i += 1
        new_node._next = temp._next
        temp._next = new_node
        self._size += 1


    def remove_first(self):
        if self.is_empty():
            print("The  list is empty")
        oh = self._head
        self._tail._next = oh._next
        self._head = oh._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return oh._data


    def remove_last(self):
        if self.is_empty():
            print("The list is empty")
        temp = self._head
        i = 1
        while i < self._size-1:
            temp = temp._next
            i += 1
        value = temp._next._data
        self._tail = temp
        self._tail._next = self._head
        self._size -= 1
        return value


    def remove_particular(self, position):
        if self.is_empty():
            print("List is empty or the position is invalid")
        temp = self._head
        i = 0
        while i < position-2:
            temp = temp._next
            i += 1
        value = temp._next._data
        temp._next = temp._next._next
        self._size -= 1
        return value


    def print_list(self):
        temp = self._head
        i = 0
        while i < self._size:
            print(temp._data, end='-->')
            temp = temp._next
            i += 1
        print()


circ_list = CircularLinkedList()
circ_list.add_first(1)
circ_list.add_last(2)
circ_list.add_last(3)
circ_list.add_last(5)
circ_list.add_particular(4, 4)
circ_list.print_list()
print(circ_list.remove_first())
circ_list.print_list()
print(circ_list.remove_last())
circ_list.print_list()
print(circ_list.remove_particular(2))
circ_list.print_list()