class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        middle_node = None
        # check for singl enode
        if self.head == self.tail:
            print("ONE NODE")
            middle_node = self.head
            return middle_node
        print("finding middle node")
        # use two pointers:
        # 1 - slow (moves one node at a time)
        # 2 - fast (moves two nodes at a time)
        slow = self.head
        fast = slow.next.next
        loops = 0
        while fast.next != None:
            print("looping")
            slow = slow.next
            fast = slow.next.next
            print(slow.value, fast.value)
            loops += 1
        total_nodes = 1 + loops + 2
        # check if even
        if total_nodes % 2 == 0:
            middle_node = slow.next
        else:
            middle_node = slow
        return middle_node


if __name__ == "__main__":
    my_linked_list = LinkedList(1)
    print(my_linked_list.find_middle_node().value)
