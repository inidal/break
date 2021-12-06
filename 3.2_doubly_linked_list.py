# 10 --> 5 --> 16

class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1


    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, value):
        new_node = Node(value)
        tmp = self.head
        holding_pointer = None

        if index >= self.length:
            self.append(value)
            return

        elif index == 0:
            self.prepend(value)
            return

        for i in range(index):
            holding_pointer = tmp
            tmp = tmp.next

        holding_pointer.next = new_node
        new_node.prev = holding_pointer
        new_node.next = tmp
        tmp.prev = new_node

        self.length += 1

    def remove(self, index):
        tmp = self.head
        holding_pointer = None

        if index >= self.length-1:
            for i in range(self.length-1):
                holding_pointer = tmp
                tmp = tmp.next
            holding_pointer.next = None
            self.tail = holding_pointer
            self.length -= 1

        elif index == 0:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            return

        else:
            for i in range(index):
                holding_pointer = tmp
                tmp = tmp.next

            tmp.next.prev = holding_pointer
            holding_pointer.next = tmp.next

            self.length -= 1

    def reverse(self):
        tmp = self.display()
        tmp_reversed = [0] * len(tmp)

        # Reset pointers
        self.head = None
        self.tail = None

        for i in range(len(tmp)):
            tmp_reversed[i] = tmp[int("-" + str(i+1))]

        for i in tmp_reversed:
            self.append(i)

    def display(self):
        tmp, lst = self.head, []
        while tmp is not None:
            lst.append(tmp.value)
            tmp = tmp.next
        return lst

l = LinkedList()
l.append(10)
l.append(5)
l.append(16)
l.prepend(1)
l.insert(2, 99)
l.insert(44, 51)
l.remove(4)
l.reverse()
print(l.display())
print(l.head.value, l.tail.value)
print(l.length)

