"""  
1. Trees: Intro and Terminology 
Trees are similar in structure to a linked list.
**Linked lists are just trees that don't fork 

Basic Structure (binary tree)
- value 
- left 
- right

Attributes:
- Full: every node in the tree either points to zero nodes or two nodes 
- Perfect: any level in the tree that has any nodes is completely filled all the way across
- Complete: tree is filled from left to right, with no gaps

Components:
- Parent
- Child 
- Leaf

Parent -> Child/Children -> Leaf/Leaves

2. Binary Search Tree

Layout: 

If a node is greater than a parent, it goes to the right. If it is less than, it goes to the left

Each new node is always compared to the top most node. Then it works its way down

3. Big O 

Best case time complexity for searching, adding, and removing items from a binary search tree is O(log n) (Divide and Conquer)

**Worst case is if a tree never forks (essentially, the structure is the same as a linked list) (O

Assumption for BST is that it will not be structures like a linked list. So, Big O run time complexity will be O(log n)  

BST vs LL 
Lookup: 
- BST = O(log n) 
- LL = O(n) 
Add:
- BST = O(log n) 
- LL:
    - Single:
        - Append = O(1) 
        - Prepend = O(1) 
    - Double: 
        - Append = O(1) 
        - Prepend = O(1)
Remove by Value:   
- BST = O(log n) 
- LL: 
    - Single = O(n)
    - Double = O

4. BST Insertion 

Steps: 
1. Create a new node
2. Compare new node to root node:
- If value of new node is less than root node go left 
- If value o new node is greater than root node go right 
3. If there is a node, repeat step two, if not, insert
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def print_tree(self):
        return


class BST:
    def __init__(self):
        # you can also create an empty tree (no need instantiate the root as 'None')
        # new_node = Node(value)
        # self.root = new_node
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        # base case
        if self.root is None:
            self.root = new_node
            return True
        current_node = self.root
        while True:
            # compare values
            if new_node.value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    return True
            elif new_node.value > current_node.value:
                if current_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    return True
            else:
                print(
                    "The new node's value cannot be equal to the values of any nodes that already exist in our tree"
                )
                return False

    def contains(self, value):
        # search for value in tree
        current_node = self.root
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True
        return False

    def print_tree():
        current_node = self.root
        if current_node is not None:
            print("ROOT: ", current_node)
        while current_node.left is not None or current_node.right is not None:
            # print left nodes
            print(current_node.left)
        return


if __name__ == "__main__":
    my_tree = BST()
    my_tree.insert(1)
    my_tree.insert(2)
    print(my_tree.contains(1))
