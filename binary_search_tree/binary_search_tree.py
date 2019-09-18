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

    # * `get_max` returns the maximum value in the binary search tree.
    # go to the right until reach Null
    # if right == None, return value
    # else keep going until null is reached
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # * `for_each` performs a traversal of _every_ node in the tree, executing
    # the passed-in callback function on each tree node value. There is a myriad of ways to
    # perform tree traversal; in this case any of them should work.
    def for_each(self, cb):
        pass
