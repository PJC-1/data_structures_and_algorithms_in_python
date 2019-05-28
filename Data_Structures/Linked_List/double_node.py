class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

node_001 = DoubleNode("Node 001")
node_001.next = DoubleNode("Node 002")
node_001.next.previous = node_001
print("node_001 value: ", node_001.value)
print("node_002 value: ", node_001.next.value)
print("node_002 previous: ", node_001.next.previous.value)
