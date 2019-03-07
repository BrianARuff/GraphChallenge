class Stack:
    def __init__(self):
        self._stack = []
        self._size = 0

    def stack(self):
        return self._stack
    
    def push(self, value):
        self._stack.append(value)
        self._size += 1

    def pop(self):
        result = self._stack.pop()
        self._size -= 1
        return result
    
    def has(self, value):
        return value in self._stack

    def get(self, value):
        result = None
        if self.has(value):
            for item in self._stack:
                if item == value:
                    result = item
                    break
        return result
            

    def size(self):
        return self._size

    def printStack(self):
        print(self._stack)
