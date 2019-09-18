
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    def __init__(self, limit=10):
        """
        Our LRUCache class keeps track of the max number of nodes it
        can hold, the current number of nodes it is holding, a doubly-
        linked list that holds the key-value entries in the correct 
        order, as well as a storage dict that provides fast access
        to every node stored in the cache.
        """
        # self.limit = limit
        # self.nodes = 0
        # self.cache = DoublyLinkedList()
        # self.storage = {}

        self.order = DoublyLinkedList()
        self.storage = dict()
        self.size = 0
        self.limit = limit

    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """
        # if self.nodes is 0 or key not in self.storage:
        #     return None
        # else:
        #     value = self.storage[key]
        #     self.cache.delete(value[1])
        #     self.cache.add_to_head([key, value[0]])
        #     return value[0]

        #pull the value out of the dict using the key
        # update position in the list
        # or return none
        if key in self.storage:
          node = self.storage[key]
          self.order.move_to_front(node)
          return node.value[1]
        else:
          return None

    def set(self, key, value):
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply 
        want to overwrite the old value associated with the key with
        the newly-specified value. 
        """
        # if key in self.storage:
        #     storage_value = self.storage[key]
        #     self.cache.delete(storage_value[1])
        #     self.cache.add_to_head([key, value])
        #     self.storage[key] = [value, self.cache.head]
        #     return
        # if self.limit is self.nodes:
        #     old_node = self.cache.tail
        #     self.cache.remove_from_tail()
        #     del self.storage[old_node.value[0]]
        #     self.nodes -= 1
        # self.cache.add_to_head([key, value])
        # self.storage[key] = [value, self.cache.head]
        # self.nodes += 1

        # if alrady exists, overwrit value - update dict
        # update dict
        # Mark as most recently used - put it in the head of the DLL

        # if at max capacity, dump oldest - remove from tail
        # Add pair to the cache - add to dict and it nodes/DLL
        if key in self.storage:
          node = self.storage[key]
          node.value = (key, value)
          self.order.move_to_front(node)
          return
        if self.size == self.limit:
          del self.storage[self.order.tail.value[0]]
          self.order.remove_from_tail()
          self.size -= 1
        self.order.add_to_head([key, value])
        self.storage[key] = self.order.head
        self.size += 1
        
        

