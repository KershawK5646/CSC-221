'''
Kyler Kershaw
11/04/19
m4HW1

Node Class File
'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __str__ (self):
        return str(self.data)

class Stack(object):
    def __init__(self):
        self.head = None

    # Push data to the top of the stack
    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            new_node.previous = None
            self.head = new_node

    # Pop data from the top of the stack
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            return temp

    def printStack(self):
        print("Stack elements:\n")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

class Que(object):
    def __init__(self):
        # self.head = None
        self.tail = None

    # Push data to the back of the Que
    def push(self, data):
        if self.tail is None:
            self.tail = Node(data)
        else:
            new_node = Node(data)
            self.tail.prev = new_node
            new_node.previous = self.tail
            new_node.next = None
            self.tail = new_node

    # Pop data from the top of the stack
    def pop(self):
        if self.tail is None:
            return None
        else:
            temp = self.tail.data
            self.tail = self.tail.previous
            return temp

    def printQue(self):
        print("Que List elements:\n")
        temp = self.tail
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.previous