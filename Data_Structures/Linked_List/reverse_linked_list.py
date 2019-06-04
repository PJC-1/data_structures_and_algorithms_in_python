class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])

def reverse(linked_list):
    reversed_linked_list = LinkedList()
    previous_node = None
    for value in linked_list:
        new_node = Node(value)
        new_node.next = previous_node
        previous_node = new_node
    reversed_linked_list.head = previous_node
    return reversed_linked_list

llist = LinkedList()
for value in [4,2,5,1,-3,0]:
    llist.append(value)

reversed = reverse(llist)
print(reversed)
