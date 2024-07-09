"""  
Stack: Intro

LIFO - Last In First Out

Stack implementations:
- List
- Linked List (Push and Pop to the "top" for O(1) run time complexity)
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        return

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return

    def pop(self):
        removed_node = None
        if self.height == 0:
            print("This is an empty stack")
            return removed_node
        elif self.height == 1:
            removed_node = self.top
            self.top = None
        else:
            removed_node = self.top
            self.top = removed_node.next
        self.height -= 1
        return removed_node

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return


"""  
2. Queue: Intro

FIFO - First in First Out
"""


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return

    def dequeue(self):
        removed_node = None
        if self.length == 0:
            print("This is an empty queue")
            return removed_node
        elif self.length == 1:
            removed_node = self.first
            self.first = None
            self.last = None
        else:
            removed_node = self.first
            self.first = removed_node.next
        self.length -= 1
        return removed_node

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
        return


if __name__ == "__main__":
    # stack
    print("STACK")
    my_stack = Stack(4)
    my_stack.push(3)
    my_stack.pop()
    my_stack.print_stack()
    # queue
    print("QUEUE")
    my_queue = Queue(4)
    my_queue.enqueue(3)
    my_queue.dequeue()
    my_queue.print_queue()
