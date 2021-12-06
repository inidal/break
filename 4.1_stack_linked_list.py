class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self): # See the very top element
        if self.length > 0:
            return self.top.value

    def push(self, value): # Add node on top of the stack
        if self.length == 0:
            new_node = Node(value)
            self.top = new_node
            self.bottom = new_node
            self.length += 1
        else:
            new_node = Node(value)
            new_node.next = self.top
            self.top = new_node
            self.length += 1


    def pop(self): # Remove from the top of the stack
            if self.length == 0:
                return
            else:
                self.top = self.top.next
                self.length -= 1

# Instantiating the Stack class
s = Stack()

# s.push('google')
# s.push('twitter')
# s.push('stackoverflow')
print(s.peek())
s.pop()
print(s.peek())
print(s.length)
