
"""
#  File: TestBinaryTree.py

#  Description:
    This Python code defines a binary search tree (BST) structure
    with methods to manipulate and analyze its nodes.

#  Student Name: Trinity Thompson

#  Student UT EID: tyt242

#  Partner Name: Marissa Shuchart

#  Partner UT EID: ms87339

#  Course Name: CS 313E

#  Unique Number: 50165

#  Date Created: 10.29.24

#  Date Last Modified: 10.29.24
"""""

import sys


class Node():
    """constructor"""
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):
        """
        This method performs a pre-order traversal of the binary tree, 
        printing the current node's data and recursively printing its 
        left and right children with indentation based on their level.
        """
        if self.lchild is not None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild is not None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        """
        The height of a binary tree is defined as the number of edges 
        on the longest path from the root node to a leaf node. If the 
        tree is empty, the height is considered to be 0.
        """
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        if self.lchild is not None:
            return 1 + self.lchild.get_height()
        if self.rchild is not None:
            return 1 + self.rchild.get_height()
        return 1


class Tree():
    """constructor"""
    def __init__(self):
        """Initializes root"""
        self.root = None

    def print(self, level):
        """Prints node at that level"""
        self.root.print_node(level)

    def get_height(self):
        """Gets height of tree"""
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        """Insert a new node with the given data into the binary search tree."""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        parent = self.root
        curr = self.root
        # finds location to insert new node
        while curr is not None:
            parent = curr
            if data < curr.data:
                curr = curr.lchild
            else:
                curr = curr.rchild
        # inserts new node based on comparision to parent node
        if data < parent.data:
            parent.lchild = new_node
        else:
            parent.rchild = new_node
        return


    def range(self):
        """
        Returns the range of values stored in a binary search tree of integers.
        The range of values equals the maximum value in the binary search 
        tree minus the minimum value.
        If there is one value in the tree the range is 0. If the tree is empty 
        the range is undefined.
        """
        if self.root is None:
            return None #undefined for an empty tree

        # Find minimum (leftmost node)
        current = self.root
        while current.lchild:
            current = current.lchild
        min_value = current.data

        # Find maximum (rightmost node)
        current = self.root
        while current.rchild:
            current = current.rchild
        max_value = current.data

        result = max_value - min_value
        return result


    def get_level(self, level):
        """Returns a list of nodes at a given level from left to right"""
        if self.root is None:
            return []

        # List to store nodes at the target level
        nodes_at_level = []

        # Use a queue for level-order traversal
        queue = [(self.root, 0)]  # Each element is (node, level)

        while queue:
            node, node_level = queue.pop(0)

            # If we find a node at our target level, add its value
            if node_level == level:
                nodes_at_level.append(node)

            # If we haven't exceeded our target level, add children to queue
            if node_level < level:
                if node.lchild:
                    queue.append((node.lchild, node_level + 1))
                if node.rchild:
                    queue.append((node.rchild, node_level + 1))

        return nodes_at_level


    def left_side_view(self):
        """
        Returns the list of the node that you see from left side
        The order of the output should be from top to down
        """
        if self.root is None:
            return []

        result = []
        level = [self.root]

        while level:
            # Add the leftmost node of current level
            result.append(level[0].data)

            # Prepare next level
            next_level = []
            for node in level:
                if node.lchild:
                    next_level.append(node.lchild)
                if node.rchild:
                    next_level.append(node.rchild)
            level = next_level

        return result


    def sum_leaf_nodes(self):
        """returns the sum of the value of all leaves.
        a leaf node does not have any children.
        """
        if self.root is None:
            return 0

        stack = [self.root]
        leaf_sum = 0

        while stack:
            node = stack.pop()

            # Check if the node is a leaf
            if node.lchild is None and node.rchild is None:
                leaf_sum += node.data
            # Push right and left children to the stack if they exist
            if node.rchild:
                stack.append(node.rchild)
            if node.lchild:
                stack.append(node.lchild)

        return leaf_sum

def make_tree(data):
    """Creates a tree instance"""
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree

# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescope will import your classes and call the methods.

def main():
    """Create three trees - two are the same and the third is different"""
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line)) 	# converts elements into ints
    t1 = make_tree(tree1_input)
    t1.print(t1.get_height())

    print("Tree range is: ",   t1.range())
    print("Tree left side view is: ", t1.left_side_view())
    print("Sum of leaf nodes is: ", t1.sum_leaf_nodes())
    print("##########################")

# Another Tree for test.
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line)) 	# converts elements into ints
    t2 = make_tree(tree2_input)
    t2.print(t2.get_height())

    print("Tree range is: ",   t2.range())
    print("Tree left side view is: ", t2.left_side_view())
    print("Sum of leaf nodes is: ", t2.sum_leaf_nodes())
    print("##########################")
# Another Tree
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line)) 	# converts elements into ints
    t3 = make_tree(tree3_input)
    t3.print(t3.get_height())

    print("Tree range is: ",   t3.range())
    print("Tree left side view is: ", t3.left_side_view())
    print("Sum of leaf nodes is: ", t3.sum_leaf_nodes())
    print("##########################")


if __name__ == "__main__":
    main()
