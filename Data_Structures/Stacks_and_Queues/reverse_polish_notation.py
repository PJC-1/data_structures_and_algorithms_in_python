class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def evaluate_post_fix(input_list):
    stack = Stack()
    for element in input_list:
        if element == '*':
            second = stack.pop()
            first = stack.pop()
            output = first * second
            stack.push(output)
        elif element == '/':
            second = stack.pop()
            first = stack.pop()
            output = int(first / second)
            stack.push(output)
        elif element == '+':
            second = stack.pop()
            first = stack.pop()
            output = first + second
            stack.push(output)
        elif element == '-':
            second = stack.pop()
            first = stack.pop()
            output = first - second
            stack.push(output)
        else:
            stack.push(int(element))
    return stack.pop()
