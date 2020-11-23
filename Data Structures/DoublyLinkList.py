class Node:
   def __init__(self, data=None):
      self.data = data
      self.next = None
      self.prev = None


class doubly_linked_list:

   def __init__(self):
      self.head = None

   def push(self, NewVal):
      NewNode = Node(NewVal)
      NewNode.next = self.head
      if self.head is not None:
         self.head.prev = NewNode
      self.head = NewNode

   def pop(self, another_Data):
       NewNode = Node(another_Data)
       NewNode.next = None
       if self.head is None:
           NewNode.prev = None
           self.head = NewNode
           return
       last = self.head
       while (last.next is not None):
           last = last.next
       last.next = NewNode
       NewNode.prev = last
       return

   def listprint(self, node):
      while (node is not None):
         print(node.data),
         last = node
         node = node.next

   def insert_after(self, prev, NewVal):
      if prev is None:
         return
      NewNode = Node(NewVal)
      NewNode.next = prev.next
      prev.next = NewNode
      NewNode.prev = prev
      if NewNode.next is not None:
         NewNode.next.prev = NewNode

   def insert_before(self, next_node, another_Data):
       if next_node is None:
           return
       NewNode = Node(another_Data)
       NewNode.prev = next_node.PrevVal
       next_node.prev = NewNode
       NewNode.next = next_node
       if NewNode.next is not None:
           next_node.PrevVal.NextVal = NewNode

   def RemoveNode(self, remove_key):
       head = self.head

       if head is not None:
           if head.data == remove_key:
               self.head = head.next
               head = None
               return
       while head is not None:
           if head.data == remove_key:
               break
           prev = head
           head = head.next
       if head == None:
           return
       prev.next = head.next
       head = None

   def RemoveFirst(self):
       self.RemoveNode(self.First())

   def RemoveLast(self):
       self.RemoveNode(self.Last())

   def First(self):
       return self.head.data

   def Last(self):
       last = self.head
       while last is not None:
           if last.next == None:
               return (last.data)
           last = last.next


def main():
    dllist = doubly_linked_list()
    dllist.push(1)
    dllist.pop(2)
    dllist.push(3)
    dllist.pop(4)

    dllist.listprint(dllist.head)

    dllist.RemoveFirst()
    dllist.insert_after(dllist.head.next, 3)
    dllist.RemoveLast()
    dllist.RemoveNode(3)

    dllist.listprint(dllist.head)
    print(dllist.First())
    print(dllist.Last())


main()