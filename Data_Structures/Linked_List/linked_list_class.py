class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search(self, value):
        if self.head is None:
            return None

        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next

        raise ValueError("Value not in the list.")

    def remove(self, value):
        if self.head is None:
            return
        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.value == value:
                node.next = node.next.next
                return
            node = node.next
        raise ValueError("Value not in the list.")

    def pop(self):
        if self.head is None:
            return None

        node = self.head
        self.head = self.head.next
        return node.value

    def insert(self, value, pos):

        if pos == 0:
            self.prepend(value)
            return

        index = 0
        node = self.head
        while node.next and index <= pos:
            if (pos - 1) == index:
                new_node = Node(value)
                new_node.next = node.next
                node.next = new_node
                return

            index += 1
            node = node.next
        else:
            self.append(value)


    def to_list(self):
        out_list = []
        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        return out_list

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend("c")
linked_list.prepend("b")
linked_list.prepend("a")
linked_list.remove("a")
linked_list.remove("b")
linked_list.remove("c")
linked_list.insert("added to the front", 0)
test = linked_list.to_list()
print(test)
