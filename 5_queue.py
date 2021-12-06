class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length > 0:
            return f"First: {self.first.value}\nLast: {self.last.value}\n"
        else:
            return

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
            self.length += 1
        else:
            new_node.next = self.last
            self.last = new_node
            self.length += 1

    def dequeue(self):
        if self.length > 0:
            tmp = self.last
            for i in range(self.length - 2):
                # self.last = self.first.next
                tmp = tmp.next
            tmp.next = None
            self.first = tmp
            self.length -= 1
        else:
            return

# Instantiate Queue class
q = Queue()

q.enqueue('google') # 1 - First
q.enqueue('twitter') # 2
q.enqueue('steam') # 3
q.enqueue('tesla') # 4 - Last
print(q.peek())
q.dequeue()
print(q.peek())
q.dequeue()
print(q.peek())
