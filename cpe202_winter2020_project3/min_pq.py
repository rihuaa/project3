"""Minimum Priority Queue
For:
    CPE202
    Sections 3 & 5
    Winter 2020
Author:
    Richard Hua
"""
class MinPQ:
    """Minimum Priority Queue
    Attributes:
        capacity (int): the capacity of the queue. The default capacity is 2,
                        but will be increased automatically.
        num_items (int): the number of items in the queue.
        arr (list): an array which contains the items in the queue.
    """
    def __init__(self, arr=None, num_items=0, capacity=2):
        self.num_items = num_items
        self.arr = arr
        self.capacity = capacity
        if self.arr is None:
            self.arr = [None] * self.capacity
        else: # arr is not None:
            self.capacity = self.num_items = len(self.arr)
            self.heapify(self.arr)

    def __eq__(self, other):
        return isinstance(other, MinPQ)\
        and (self.arr == other.arr)\
        and (self.capacity == other.capacity)\
        and (self.num_items == other.num_items)

    def __repr__(self):
        return 'MinPQ(capacity=%s, num_items=%s, arr=%s)'\
        % (self.capacity, self.num_items, self.arr)

    def heapify(self, arr):
        """initialize the queue with a given array and conver the array into a min heap
        Args:
            arr (list): an array
        Returns:
            None : it returns nothing
        """
        parent = self.index_parent(self.num_items - 1)
        while parent != 0:
            self.shift_down(parent)
            parent = self.index_parent(parent)
        self.shift_down(parent)


    def insert(self, item):
        """inserts an item to the queue
        If the capacity == the num_items before inserting an item, enlarge the array.

        Args:
            item (any): an item to be inserted to the queue. It is of any data type.
        Returns:
            None : it returns nothing
        """
        if self.capacity == self.num_items:
            self.enlarge()
        self.arr[self.num_items] = item
        self.num_items += 1
        self.shift_up(self.num_items - 1)

    def del_min(self):
        """deletes the minimum item in the queue
        If the capacity > 2 and num_items > 0 and <= capacity // 4, shrink the array

        Returns:
            any : it returns the minimum item, which has just been deleted
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.is_empty():
            raise IndexError
        if self.num_items == 1:
            self.num_items -= 1
            return self.arr[0]
        min = self.arr[0]
        self.arr[0] = self.arr[self.num_items - 1]
        self.num_items -= 1
        self.shift_down(0)
        if self.capacity > 2 and self.num_items and self.capacity >= self.num_items * 4:
            self.shrink()
        return min

    def min(self):
        """returns the minimum item in the queue without deleting the item
        Returns:
            any : it returns the minimum item
        Raises:
            IndexError : Raises IndexError when the queue is empty
        """
        if self.is_empty():
            raise IndexError
        return self.arr[0]

    def is_empty(self):
        """checks if the queue is empty
        Returns:
            bool : True if empty, False otherwise.
        """
        if self.size():
            return False
        return True

    def size(self):
        """returns the number of items in the queue
        Returns:
            int : it returns the number of items in the queue
        """
        return self.num_items

    def enlarge(self):
        """enlarges the array.
        """
        self.arr = self.arr + [None]*self.capacity
        self.capacity = 2*self.capacity
        return self.arr

    def shrink(self):
        """shrinks the array.
        """
        self.arr = self.arr[:len(self.arr)//2]
        self.capacity = self.capacity // 2
        return self.arr

    def shift_up(self, idx):
        """shifts up an item in the queue using tail recursion.
        Use only < operator to compare two items: do not use <=, >, >=.

        Args:
            idx (int): the index of the item to be shifted up in the array.

        Returns:
            None : it returns nothing
        """
        parent = self.index_parent(idx)
        while parent >= 0 and self.arr[idx] < self.arr[parent]:
            self.arr[idx], self.arr[parent] = self.swap(self.arr[idx], self.arr[parent])
            idx = parent
            parent = self.index_parent(idx)
        # self.shift_down(0)
        # if parent < 0:
        #     return
        # while self.arr[idx] < self.arr[parent]:
        #     self.arr[idx], self.arr[parent] = self.swap(self.arr[idx], self.arr[parent])
        #     idx = parent
        #     parent = self.index_parent(idx)
        #     if parent < 0:
        #         return
        #         # shift_down(0)


    def shift_down(self, idx):
        """shifts down an item in the queue using tail recursion.
            Use only < operator to compare two items: do not use <=, >, >=.
            ​YOU NEED TO DETERMINE WHERE THE END OF THE HEAP IS.
            YOU CAN USE self.num_items FOR DOING SO.

            Args:
                idx (int): the index of the item to be shifted down in the array.

            Returns:
                None : it returns nothing
        """
        left = self.index_left(idx)
        right = self.index_right(idx)
        end = self.num_items
        # print('left', left)
        # print('right', right)
        # print('idx', idx)
        # print('num items', self.num_items)
        while left <= end and right <= end and \
        (self.arr[left] < self.arr[idx] or \
        self.arr[right] < self.arr[idx]):
            if self.arr[left] < self.arr[idx]:
                self.arr[left], self.arr[idx] = self.swap(self.arr[left], self.arr[idx])
                idx = left
                # if left > end:
                #     break
            elif self.arr[right] < self.arr[idx]:
                self.arr[right], self.arr[idx] = self.swap(self.arr[right], self.arr[idx])
                idx = right
                # if right > end:
                #     break
            else:
                break
            left = self.index_left(idx)
            right = self.index_right(idx)

    def swap(self, a, b):
        temp = a
        a = b
        b = temp
        return a, b

    def index_left(self, idx):
        """returns the index of the left child

        Args:
            idx (int): the index of the node

        Returns:
            int : it returns the index of the left child
        """
        return 2*idx + 1


    def index_right(self, idx):
        """returns the index of the right child

        Args:
            idx (int): the index of the node

        Returns:
            int : it returns the index of the right child
        """
        return 2*idx + 2


    def index_parent(self, idx):
        """returns the index of the parent

        Args:
            idx (int): the index of the node

        Returns:
            int : it returns the index of the parent
        """
        return (idx - 1) // 2


    def index_minchild(self, left, right, end):
        """returns the index of the min child

        Args:
            left (int): the index of the left child
            right (int): the index of the right child
            end (int): the end index of the heap

        Returns:
            int : it returns the index of the min child
        """
        return min(left, right, end)
