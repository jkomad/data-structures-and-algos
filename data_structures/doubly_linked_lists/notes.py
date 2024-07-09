class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        removed_node = None
        if self.length == 0:
            print("This list is empty")
            return removed_node
        elif self.length == 1:
            removed_node = self.tail
            self.head = None
            self.tail = None
        else:
            removed_node = self.tail
            prev = removed_node.prev
            prev.next = None
            removed_node.prev = None
            self.tail = prev
        self.length -= 1
        return removed_node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return

    def pop_first(self):
        removed_node = None
        if self.length == 0:
            print("This list is empty")
            return removed_node
        elif self.length == 1:
            removed_node = self.head
            self.head = None
            self.tail = None
        else:
            removed_node = self.head
            new_head = self.head.next
            self.head.next = None
            new_head.prev = None
            self.head = new_head
        self.length -= 1
        return removed_node

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            mid_pt = round(self.length / 2)
            if index < mid_pt:
                # start from head
                temp = self.head
                for _ in range(index):
                    temp = temp.next
            else:
                # go back from tail
                temp = self.tail
                for _ in range(self.length - 1, index, -1):
                    temp = temp.prev
        return temp

    def set_value(self, index, value):
        if index < 0 or index > self.length:
            return None
        else:
            # get target node
            node = self.get(index)
            node.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            # prepend
            return self.prepend(value)
        elif index == self.length:
            # append
            return self.append(value)
        else:
            new_node = Node(value)
            tgt_node = self.get(index)
            prev = tgt_node.prev
            prev.next = new_node
            new_node.next = tgt_node
            tgt_node.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        removed_node = None
        if index < 0 or index >= self.length:
            return None
        if self.length == 0:
            return removed_node
        else:
            if index == 0:
                # pop_first
                return self.pop_first()
            elif index == self.length - 1:
                # pop
                return self.pop()
            else:
                removed_node = self.get(index)
                print(removed_node.prev.next.value)
            self.length -= 1
        return removed_node

    def print_list(self):
        temp = self.head
        idx = 0
        while temp is not None:
            print(f"INDEX: {idx}; VALUE: {temp.value}")
            temp = temp.next
            idx += 1
        return


if __name__ == "__main__":
    my_dll = DoublyLinkedList(0)
    my_dll.append(1)
    my_dll.append(2)
    my_dll.append(3)
    my_dll.set_value(2, 100)
    my_dll.insert(4, 500)
    my_dll.remove(4)
    my_dll.print_list()
