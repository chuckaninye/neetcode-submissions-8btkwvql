class MyHashSet:

    def __init__(self):
        self.s = []

    def add(self, key: int) -> None:
        if key in self.s:
            return
        else:
            self.s.append(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            for i, n in enumerate(self.s):
                if n == key:
                    del self.s[i]
        else:
            return
            

    def contains(self, key: int) -> bool:
        return key in self.s


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)