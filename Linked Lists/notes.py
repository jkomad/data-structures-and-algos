# 1. Big 0

# Append to end of linked list = 0(1)
# The number of operations required to add to the end of a linked list is constant

# Pop an item from the end of a linked list = 0(n)
# You must iterate through the entirety of a linked list in order to remove an item from the end

# Append item to front = 0(1)
# Number of operations is constant

# Remove item from front = 0(1)
# Number of operations is constant

# Add item somewhere in the middle = 0(n)
# Requires iteration through list

# Remove item somewhere in the middle = 0(n)
# Requires iteration through list

# Look up (by value or index) = 0(n)

# Key Differences between Linked Lists and Python native lists
# Pop:
# Linked List = 0(n)
# List = 0(1)

# Lookup by Index:
# Linked List = 0(n)
# List = 0(n1)

# Prepend:
# Linked List = 0(1)
# List = 0(n)

# Pop First:
# Linked List = 0(1)
# List = 0(n)

# 2. Under the hood

# What is a Node

# A node is essentially a dictionary composed of two parts: the vale and the node pointer

# 3. Constructors


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        # create a new instance of linked list and create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        # create new node
        new_node = Node(value)
        # check for edge cases
        # if length == 0 (set head and tail to new node)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return

    def pop(self):
        removed_node = None
        # if list is empty return None
        if self.length == 0:
            print("EMPTY LIST")
            return removed_node
        elif self.length == 1:
            removed_node = self.tail
            self.head = None
            self.tail = None
        else:
            removed_node = self.tail
            # iterate through list to find new tail
            temp_head = self.head
            temp_tail = temp_head.next
            while temp_tail.next != None:
                temp_head = temp_head.next
                temp_tail = temp_head.next
            temp_head.next = None
            self.tail = temp_head
        self.length -= 1
        print("REMOVED NODE: ", removed_node.value)
        return removed_node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head, self.tail = new_node, new_node
        else:
            old_head = self.head
            new_node.next = old_head
            self.head = new_node
        self.length += 1
        return

    def pop_first(self):
        # default
        removed_node = None
        if self.length == 0:
            return removed_node
        elif self.length == 1:
            removed_node = self.head
            self.head = None
            self.tail = None
        else:
            removed_node = self.head
            self.head = removed_node.next
            removed_node.next = None
        self.length -= 1
        return removed_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    def set_value(self, index, value):
        # check for valid index
        if index < 0 or index >= self.length:
            return None
        else:
            # get value
            node = self.get(index)
            node.value = value
        return

    def insert(self, index, value):
        # check for valid index
        if index < 0 or index > self.length:
            return None
        if self.length == 0:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        else:
            # check if index is 0
            if index == 0:
                self.prepend(value)
            elif index == self.length:
                self.append(value)
            else:
                new_node = Node(value)
                prior_node = self.get(index - 1)
                old_node = prior_node.next
                prior_node.next = new_node
                new_node.next = old_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            if index == 0:
                return self.pop_first()
            elif index == self.length - 1:
                return self.pop()
            else:
                removed_node = self.get(index)
                prior_node = self.get(index - 1)
                prior_node.next = removed_node.next
                removed_node.next = None
            self.length -= 1
        return removed_node

    def reverse(self):
        print("REVERSING")
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
        return

    def print_list(self):
        if self.length == 0:
            print("THIS IS AN EMPTY LINKED LIST")
        else:
            temp = self.head
            idx = 0
            print("LOOPING THROUGH LINKED LIST ")
            while temp is not None:
                print(f"INDEX: {idx}; VALUE: {temp.value}")
                temp = temp.next
                idx += 1
            print("END OF LINKED LIST")


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.insert(2, 100)
    my_linked_list.set_value(0, 500)
    my_linked_list.reverse()
    my_linked_list.print_list()
