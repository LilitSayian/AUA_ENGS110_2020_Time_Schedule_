class Deque:
    def __init__(self, size):
        self.size = size
        self.rear = -1
        self.front = -1
        self.CyclicArray = [None for i in range(size)]

    def AddFirst(self, obj):
        if ((self.rear + 1) % self.size == self.front):
            for i in range(self.size):
                self.CyclicArray.append(None)
            self.size = self.size * 2
            self.front = (self.front - 1) % self.size
            self.CyclicArray[self.front] = data

        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.CyclicArray[self.front] = obj
        else:
            self.front = (self.front - 1) % self.size
            self.CyclicArray[self.front] = obj

    def AddLast(self, obj):
        if ((self.rear + 1) % self.size == self.front):
            for i in range(self.size):
                self.CyclicArray.append(None)
            self.size = self.size * 2
            self.rear = (self.rear + 1) % self.size
            self.CyclicArray[self.rear] = obj
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.CyclicArray[self.rear] = obj
        else:
            self.rear = (self.rear + 1) % self.size
            self.CyclicArray[self.rear] = obj

    def removeFirst(self):
        if (self.front == -1):
            # return
            print("Empty\n")

        elif (self.front == self.rear):
            temp = self.CyclicArray[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.CyclicArray[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def removeLast(self):
        if (self.front == -1):
            print("Empty\n")

        elif (self.front == self.rear):
            temp = self.CyclicArray[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.CyclicArray[self.rear]
            self.rear = (self.rear - 1) % self.size
            return temp

    def first(self):
        print(self.CyclicArray[self.front])

    def last(self):
        print(self.CyclicArray[self.rear])

    def display(self):
        if (self.front == -1):
            # return
            print("Empty")

        elif (self.rear >= self.front):
            print("Cyclic array contains:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.CyclicArray[i], end=" ")
            print()

        else:
            print("Cyclic array contains:", end=" ")
            for i in range(self.front, self.size):
                print(self.CyclicArray[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.CyclicArray[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("It's Full")


def main():
    cyclicArray = Deque(6)
    cyclicArray.AddFirst("1")
    cyclicArray.AddFirst("2")
    cyclicArray.AddFirst("3")
    cyclicArray.AddLast("4")
    cyclicArray.AddLast("5")
    cyclicArray.first()
    cyclicArray.last()
    cyclicArray.display()

main()