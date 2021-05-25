class SuperStack:

    def __init__(self, size=-1):
        self._max_size = size
        self._stack = []

    def push(self, num):
        if num.is_integer():
            if self.is_full():
                print("the stack full, can't push any more!")
            else:
                self._stack.append(num)

    def pop(self):
        if self.is_empty():
            print("The stack is empty!")
        else:
            ret = self._stack[-1]
            self._stack = self._stack[:-1]
            return ret

    def top(self):
        if self.is_empty():
            print("The stack is empty!")
        else:
            return self._stack[-1]

    def is_empty(self):
        return len(self._stack) == 0

    def is_full(self):
        # if max_size== -1 return False...
        return len(self._stack) == self._max_size

    def max(self):
        if self.is_empty():
            print("The stack is empty!")
            return None
        return max(self._stack)

    def min(self):
        if self.is_empty():
            print("The stack is empty!")
            return None
        return min(self._stack)
