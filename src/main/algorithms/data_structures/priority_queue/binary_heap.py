from collections import defaultdict


class PQueue:
    def __init__(self, **kwargs):
        self.heap_size = 0
        self.heap_capacity = kwargs.get('capacity', 0)
        self.heap = [None] * self.heap_capacity
        # Map will be used to map the index of different elements
        # The value is a list, to handle the duplicate elements
        self.map = defaultdict(list)
        # Costruct the heap by heapifying the input array
        if 'elems' in kwargs:
            self.heap = kwargs.get('elems')
            for i, elem in enumerate(self.heap):
                self.map[elem].append(i)
            # Set both the heap size and capacity as the no. of elements
            self.heap_size = self.heap_capacity = len(self.heap)
            # Heapify process: Start from the first non-leaf node
            non_leaf_index = int(self.heap_size/2) - 1
            # Why start sinking from last non-leaf?
            # Because in for the last non-leaf it is as simple as a single swap
            # On top of this we build up the sinking process for each non-leaf node
            for i in range(max(0, non_leaf_index), -1, -1):
                self.sink(i)
    
    def sink(self, k):
        while True:
            left, right = 2 * k + 1, 2 * k + 2
            # Assume left child is the smallest one
            smallest = left 
            # If right child is less than left child then right child
            # is the smallest one
            if right < self.heap_size and self.heap[right] < self.heap[left]:
                smallest = right 
            # Break if left index is greater than heap size or if left 
            # child value is already greater than the root's value
            if smallest >= self.heap_size or self.heap[smallest] > self.heap[k]:
                break
            # swap the nodes (k, smallest)
            self.swap(k, smallest)
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
        # Get the index of the parent
        parent = int((k - 1) / 2)
        # If we are not at the root and parent's value
        # is greater than current node's value then swap
        while k > 0 and self.heap[parent] > self.heap[k]:
            self.swap(parent, k)
            k = parent
            parent = int((k - 1) / 2)
    
    def swap(self, i, j):
        i_val, j_val = self.heap[i], self.heap[j]
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.map_swap(i_val, j_val, i, j) 

    # Swap two values and their indices in the map
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
        removed_data = self.heap[index]
        self.swap(index, self.heap_size - 1)
        self.remove_last()
        parent = int((index - 1) / 2)
        # If parent is greater than current value
        # Then swim current value up
        if self.heap[parent] > self.heap[index]:
            self.swim(index)
        # Else sink it down
        else:
            self.sink(index)
        return removed_data
        
    def remove_last(self):
        if self.is_empty():
            raise RuntimeError("Empty Heap")
        last_elem = self.heap[self.heap_size - 1]
        self.map[last_elem].remove(self.heap_size - 1)
        self.heap[self.heap_size - 1] = None
        self.heap_size -= 1

    def is_min_heap(self, k):
        # If we are outside the heap_size, return True
        if k >= self.heap_size:
            return True
        left = 2 * k + 1
        right = 2 * k + 2
        if self.heap[k] > self.heap[left] or self.heap[k] > self.heap[right]:
            return False
        return self.is_min_heap(left) and self.is_min_heap(right)

    def print_pq(self):
        print(self.heap)


if __name__ == "__main__":
    elems = [9, 10, 4, 5, 1, 2, 2]
    pq = PQueue(elems=elems)
    pq.print_pq()
    pq.add(6)
    pq.add(-4)
    pq.add(-1)
    pq.print_pq()
    print(pq.poll())
    print(pq.peek())
    print(pq.remove(-4))
    print(pq.poll())
    pq.print_pq()
    print(pq.peek())

    pq = PQueue(capacity = 4)
    pq.print_pq()
    pq.add(6)
    pq.add(-4)
    pq.add(-1)
    pq.print_pq()
    print(pq.poll())
    print(pq.peek())
    print(pq.remove(-4))
    print(pq.poll())
    pq.print_pq()
    print(pq.peek())