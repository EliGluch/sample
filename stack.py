class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, obj):
        self.stack.append(obj)
        return

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def push_n(self, list):
        self.stack = self.stack + list
        return

    def pop_n(self, n):
        list = self.stack[-n:]
        self.stack = self.stack[:-n]
        return list

    def stack_print(self):
        print(self.stack)


s = Stack()
s.push(10)
s.push_n([1,2,3,4,6,7,8])
s.stack_print()

