class MinStack:

    def __init__(self):
        self.stack = []
        self.arr = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if len(self.arr) > 0:
            minVal = min(self.arr[-1], val)
            self.arr.append(minVal)
        else:
            self.arr.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.arr[-1]
