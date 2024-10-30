

#  File: TestBinaryTree.py

#  Description: This Python code defines a binary search tree (BST) structure with methods to manipulate and analyze its nodes. 

#  Student Name: Trinity Thompson

#  Student UT EID: tyt242

#  Partner Name: Marissa Shuchart

#  Partner UT EID: ms87339

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created: 10.29.24

#  Date Last Modified: 10.29.24


import sys


class Node():
    # constructor
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def print_node(self, level=0):

        if self.lchild != None:
            self.lchild.print_node(level + 1)

        print(' ' * 3 * level + '->', self.data)

        if self.rchild != None:
            self.rchild.print_node(level + 1)

    def get_height(self):
        if self.lchild is not None and self.rchild is not None:
            return 1 + max(self.lchild.get_height(), self.rchild.get_height())
        elif self.lchild is not None:
            return 1 + self.lchild.get_height()
        elif self.rchild is not None:
            return 1 + self.rchild.get_height()
        return 1


class Tree():
    # constructor
    def __init__(self):
        self.root = None

    def print(self, level):
        self.root.print_node(level)

    def get_height(self):
        return self.root.get_height()

    # Inserts data into Binary Search Tree and creates a valid BST
    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        else:
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

    # Returns the range of values stored in a binary search tree of integers.
    # The range of values equals the maximum value in the binary search tree minus the minimum value.
    # If there is one value in the tree the range is 0. If the tree is empty the range is undefined.
    def range(self):
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

        return max_value - min_value

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        nodes_at_level = []

        def traverse(node, current_level):
            if node is None:
                return 
            # If wer're at the target level, add this node's value
            if current_level == level:
                nodes_at_level.append(node.data)
                return
            # If we havent reaches the target level yet, keep going 
            elif current_level < level:
                # Visit left child first 
                traverse(node.lchild, current_level + 1)
                # Visit right child 
                traverse(node.rchild, current_level + 1)
        
        # Start traversal from the root at level 0 
        traverse(self.root, 0)
        return nodes_at_level 


    # Returns the list of the node that you see from left side
    # The order of the output should be from top to down
    def left_side_view(self):
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


    # returns the sum of the value of all leaves.
    # a leaf node does not have any children.
    def sum_leaf_nodes(self):
        def sum_leaves(node):
            if node is None:
                return 0
            # If this is a leaf node, return its value
            if node.lchild is None and node.rchild is None:
                return node.data
            # Otherwise, sum up leaves in left and right subtrees
            return sum_leaves(node.lchild) + sum_leaves(node.rchild)
        
        return sum_leaves(self.root)
  
def make_tree(data):
    tree = Tree()
    for d in data:
        tree.insert(d)
    return tree


# Develop your own main function or test cases to be able to develop.
# Our tests on the Gradescop will import your classes and call the methods.

def main():
    # Create three trees - two are the same and the third is different
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



