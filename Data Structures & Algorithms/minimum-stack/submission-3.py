class MinStack:

    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, value: int) -> None:
        self.st.append(value)
        if self.minSt:
            self.minSt.append(min(self.minSt[-1], value))
        else:
            self.minSt.append(value)

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
