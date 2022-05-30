from collections import defaultdict


class PQueue:
    def __init__(self, capacity=0, **kwargs):
        self.heap_size = 0
        self.heap_capacity = capacity
        self.heap = []
        self.map = defaultdict(list)
        # Costruct the heap by heapifying the input array
        if 'elems' in kwargs:
            self.heap = kwargs.get('elems')
            # Set both the heap size and capacity as the no. of elements
            self.heap_size = self.heap_capacity = len(self.heap)
            # Heapify process: Start from the first non-leaf node
            for i in range(max(0, self.heap_size/2 - 1), -1, -1):
                self.sink(i)
            for i, elem in enumerate(self.heap):
                self.map[elem].append(i)
    
    def sink(self, k):
        while True:
            left, right = 2 * k + 1, 2 * k + 2
            smallest = left # Assume left child is the smallest one
            # If right child is less than left child then right child
            # is the smallest one
            if right < self.heap_size and self.heap[right] < self.heap[left]:
                smallest = right 
            # Break if left index is greater than heap size or if left 
            # child value is already greater than the root's value
            if left >= self.heap_size or self.heap[left] > self.heap[k]:
                break
            # swap the nodes (k, smallest)
            self.heap[k], self.heap[smallest] = self.heap[smallest], self.heap[k]
            k = smallest

    def is_empty(self):
        return self.heap_size == 0

    def clear(self):
        self.heap = [None for _ in range(self.heap_capacity)] 
        self.map.clear()
        self.heap_size = 0

    def size(self):
        return self.heap_size

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Empty Heap")
        return self.heap[0]
    
    def poll(self):
        if self.is_empty():
            raise RuntimeError("Empty Heap")
        return self.remove_at(0)

    def contains(self, elem):
        if not elem:
            return False
        return True if elem in self.map else False

    def add(self, elem):
        if not elem:
            raise ValueError("Null element")
        if self.heap_size < self.heap_capacity:
            self.heap[self.heap_size] = elem
        else:
            self.heap.append(elem)
            self.heap_capacity += 1
        self.map[elem].append(self.heap_size)
        self.swim(self.heap_size)
        self.heap_size += 1

    def swim(self, k):
        parent = int((k - 1) / 2)
        while k > 0 and self.heap[parent] > self.heap[k]:
            self.swap(parent, k)
            k = parent
            parent = int((k - 1) / 2)
    
    def swap(self, i, j):
        i_val, j_val = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.map_swap(i_val, j_val, i, j) 

    def map_swap(self, i_val, j_val, i, j):
        self.map[i_val].remove(i)
        self.map[i_val].append(j)
        self.map[j_val].remove(j)
        self.map[j_val].append(i)

    def map_get(self, elem):
        index = None
        if elem in self.map and len(self.map[elem]) > 0:
            index = self.map[elem][0]
        return index

    def remove(self, elem):
        if not elem:
            return False
        index = self.map_get(elem)
        if index:
            self.remove_at(elem)
        return True if index else False
    
    def remove_at(self, index):
        self.swap(index, self.heap_size)
        self.remove_last()
        

    def remove_last(self):
        if self.is_empty():
            raise RuntimeError("Empty Heap")
        last_elem = self.heap[self.heap_size]
        self.map[last_elem].remove(self.heap_size)
        self.heap[self.heap_size] = None
        self.heap_size -= 1


