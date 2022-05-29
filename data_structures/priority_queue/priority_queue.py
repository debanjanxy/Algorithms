class PQueue:
    def __init__(self, capacity=0, **kwargs):
        self.heap_size = 0
        self.heap_capacity = capacity
        self.heap = []
        self.map = {}

        # Costruct the heap by heapifying the array
        if 'elems' in kwargs:
            self.elems = kwargs.get('elems')
            self.heap_size = self.heap_capacity = len(self.elems)
            self.heap = [float('inf')] * self.heap_capacity
            for i, elem in enumerate(self.elems):
                self.map[elem] = i
                self.heap[i] = elem
            # Heapify process
        






    