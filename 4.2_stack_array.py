class Stack:
    def __init__(self):
        self.array = []

    def peek(self): # See the very top element
        return self.array[-1]

    def push(self, value): # Add node on top of the stack
        self.array.append(value)

    def pop(self): # Remove from the top of the stack
        self.array.pop()

    def length(self):
        print(len(self.array))

# Instantiating the Stack class
s = Stack()

s.push('google')
s.push('twitter')
s.push('stackoverflow')
print(s.peek())
s.pop()
print(s.peek())
s.length()
