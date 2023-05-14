class Stack():
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) <= 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.stack[len(self.stack) - 1]