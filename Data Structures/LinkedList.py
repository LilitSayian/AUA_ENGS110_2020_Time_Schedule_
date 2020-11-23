from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insertFirst(self, data):
        pass

    @abstractmethod
    def removeFirst(self):
        pass

    @abstractmethod
    def insertLast(self, data):
        pass

    @abstractmethod
    def removeLast(self):
        pass

    @abstractmethod
    def getfirst_(self):
        pass

    @abstractmethod
    def getlast_(self):
        pass

    @abstractmethod
    def insert_Before(self, data, data_to_check):
        pass

    @abstractmethod
    def insert_After(self, data, data_to_check):
        pass

    @abstractmethod
    def remove(self, data):
        pass

    @abstractmethod
    def indexOf(self, data):
        pass

    @abstractmethod
    def getsize_(self):
        pass

class Node:
    def __init__(self, data, next, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

    def __str__(self):
        return self.data

class Single_Linked_List(ListADT):
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def insertFirst(self, obj):
        node = Node(obj, self._first)
        self._first = node
        if self._last == None:
            self._last = node
        self._size += 1

    def removeFirst(self):
        if self._first == None:
            return
        if self._size == 1:
            self._first = None
            self._last = None
            self._size -= 1
            return
        tmp = self._first
        self._first = self._first.next
        tmp.next = None
        self._size -= 1

    def insertLast(self, obj):
        node = Node(obj, None)
        if self._last == None:
            self._first = node
            self._last = node
            self._size += 1
            return
        self._last.next = node
        self._last = node
        self._size += 1

    def removeLast(self):
        if self._size == 0:
            return
        if self._size == 1:
            self._first = None
            self._last = None
            self._size -= 1
            return
        tmp = self._first
        # Iterate over the linked list to get a reference of the pre-last element
        while tmp.next != self._last:
            tmp = tmp.next

        tmp.next = None
        self._last = tmp
        self._size -= 1

    def getsize_(self):
        return self._size

    def getfirst_(self):
        return self._first

    def getlast_(self):
        return self._last

    def __iter__(self):
        self._cursor = self._first
        return self

    def __next__(self):
        if self._cursor == None:
            raise StopIteration
        c = self._cursor
        self._cursor = self._cursor.next
        return c

    def insert_Before(self, data, check_data):
        if self.first and self.last:
            current_ = self.first
            previous_ = None
            while current_ is not None:
                if current_.data == check_data:
                    new_node = Node(data, current_)
                    if previous_ is None:
                        self.first = new_node
                    else:
                        previous_.next = new_node
                    self.size += 1
                    return
                else:
                    previous_ = current_
                    current_ = current_.next
        else:
            print("The List is empty")

    def insert_After(self, data, check_data):
        if self.first and self.last:
            current_ = self.first
            while current_ is not None:
                if current_.data == check_data:
                    new_ = Node(data, current_.next)
                    if current_.next is None:
                        current_.next = new_
                        self.last = new_
                    else:
                        current_.next = new_
                    self.size += 1
                    return
                else:
                    current_ = current_.next
        else:
            print("List is empty")

    def remove(self, data):
        current_ = self.first
        previous_ = None
        while current_ is not None:
            if current_.data == data:
                if previous_ is not None:
                    previous_.next = current_.next
                else:
                    self.first = current_.next
                self.size -= 1
                return
            else:
                previous_ = current_
                current_ = current_.next

    def indexOf(self, data):
        current_ = self.first
        index = 0
        while current_.next is not None:
            if current_.data == data:
                return index
            else:
                current_ = current_.next
                index += 1
        print("No such data")

sl = Single_Linked_List()
sl.insertFirst("a")
sl.insertFirst("b")
sl.insertFirst("c")
sl.insertFirst("d")
sl.insertFirst("e")

for e in sl:
    print(e)

it = iter(sl)

print("Using iter() and next() methods")
while True:
    try:
        print(next(it))
    except StopIteration:
        break


def printObj(ItObj):
    print("printing elements of iterable object " + ItObj.__class__.__name__)
    for i in ItObj:
        print(i)


l = [1, 6, 7, 8]
s = "datastructures"

printObj(s)
printObj(l)
printObj(sl)

