import sys
sys.path.append('../queue_and_stack')

from dll_stack import Stack
from dll_queue import Queue


# Questions:
# Only ints?
# Negative numbers?

# Observations
# >= goes right
# Need to traverse to delete
# When deleting, the smallest child becomes parent


class BinarySearchTree:
    def __init__(self, value):  # We're just using value, so key is value
        self.value = value
        self.left = None
        self.right = None

    # * `insert` adds the input value to the binary search tree, adhering to the
    # rules of the ordering of elements in a binary search tree.
    # Need to traverse to find spot to insert
    # compare given value with root
    # if value is present at root, return root
    # if value is > root, go to the right, otherwise go to the left
    def insert(self, value):
        new_value = BinarySearchTree(value)
        if value < self.value:
            if self.left == None:
                self.left = new_value
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = new_value
            else:
                self.right.insert(value)

        # Current node is self
        # Check if self.value is bigger or smaller than new value - left or right
        # We go left or right, then check if node exists
        # if node does not exist then create a node there
        # if node does exist use recursion! Call insert on that node
        # if value < self.value:
        #     if not self.left:
        #         self.left = BinarySearchTree(value)
        #     else:
        #         self.left.insert(value)
        # else:
        #     if not self.right:
        #         self.right = BinarySearchTree(value)
        #     else:
        #         self.right.insert(value)
        



    # * `contains` searches the binary search tree for the input value,
    # returning a boolean indicating whether the value exists in the tree or not.
    # Start from root and traverse the tree
    # We can stop at the first instance of a value
    # We know it's not found if we get to a node that doesn't have children
    # target == root, return true
    # target < root, go left
    # target > root, go right
    # if target is found return true, else return false
    def contains(self, target):
        if target == self.value:
            return True
        else:
            if target < self.value:
                if self.left == None:
                    return False
                return self.left.contains(target)
            else:
                if self.right == None:
                    return False
                return self.right.contains(target)

    # Check if the current value is the target, if so we're done
    # otherwise, left or right based on bigger or smaller, then 
    # call contains again
        # if self.value == target:
        #     return True
        # else:
        #     if target < self.value:
        #         if not self.left:
        #             return False
        #         else:
        #             return self.left.contains(target)
        #     else:
        #         if not self.right:
        #             return False
        #         else:
        #             return self.right.contains(target)
    

    # * `get_max` returns the maximum value in the binary search tree.
    # go to the right until reach Null
    # if right == None, return value
    # else keep going until null is reached
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

        # # max node is farthest to the right
        # if not self.right:
        #     return self.value
        # return self.right.get_max()


    # * `for_each` performs a traversal of _every_ node in the tree, executing
    # the passed-in callback function on each tree node value. There is a myriad of ways to
    # perform tree traversal; in this case any of them should work.
    def for_each(self, cb):
        cb(self.value)
        if self.left != None:
            self.left.for_each(cb)
        if self.right != None:
            self.right.for_each(cb)

        # cb(self.value)
        # if self.left:
        #     self.left.for_each(cb)
        # if self.right:
        #     self.right.for_each(cb)



# DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_dft(self, node):
        if node.left:
            node.in_order_dft(node.left)
        print(node.value)
        if node.right:
            node.in_order_dft(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        qu = Queue()
        qu.enqueue(node)
        current_node = node
        while qu.len() is not 0:
            current_node = qu.dequeue()
            print(current_node.value)
            if current_node.left:
                qu.enqueue(current_node.left)
            if current_node.right:
                qu.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        s = Stack()
        s.push(node)
        current_node = node
        while s.len() is not 0:
            current_node = s.pop()
            print(current_node.value)
            if current_node.left:
                s.push(current_node.left)
            if current_node.right:
                s.push(current_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

