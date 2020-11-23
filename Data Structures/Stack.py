class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # def __init__(self):
        # self.stack = []
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            node.next = self.head
            self.head = node

    def pop(self):
        if self.isempty():
            return None
        else:
            node_pop = self.head
            self.head = self.head.next
            node_pop.next = None
            return node_pop.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        _node = self.head
        if self.isempty():
            print("The stack is empty")
        else:
            while (_node != None):
                print(_node.data, ",", end=" ")
                _node = _node.next
            return

def main():

    Stack_ = Stack()
    Stack_.push(1)
    Stack_.push(2)
    Stack_.push(3)
    Stack_.push(4)
    Stack_.push(5)

    Stack_.display()
    print("\n")

    print("\nTop element of the stack is:", Stack_.peek())
    print("\n")

    Stack_.pop()
    Stack_.pop()

    Stack_.display()
    print("\n")

    print("\nTop element of the stack is: ", Stack_.peek())


main()
