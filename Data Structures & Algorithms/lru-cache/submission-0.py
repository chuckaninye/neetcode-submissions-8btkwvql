class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            oldNode = self.cache[key]
            self.remove(oldNode)

        node = ListNode(key, value)
        self.add(node)
        self.cache[key] = node

        if len(self.cache) > self.cap:
            nodeToRemove = self.head.next
            self.remove(nodeToRemove)
            del self.cache[nodeToRemove.key]
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        prevNode = self.tail.prev
        prevNode.next = node
        node.prev = prevNode
        node.next = self.tail
        self.tail.prev = node