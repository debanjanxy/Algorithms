from linked_list.linked_list import DoublyLinkedList


# class Queue:
#     def __init__(self):
#         self.dll = DoublyLinkedList()
#         self.size = 0

#     def enque(self, elem):
#         self.dll.add_last(elem)
#         self.size += 1

#     def deque(self):
#         if self.is_empty():
#             raise RuntimeError("Empty Queue")
#         elem = self.dll.remove_first()
#         self.size -= 1

#     def is_empty(self):
#         return self.size == 0

#     def print_que(self):
#         print(self.dll.to_string())

#     def peek(self):
#         if self.is_empty():
#             raise RuntimeError("Empty Queue")
#         return self.dll.peek_first()

# Static array implementation
class Queue:
    def __init__(self, size):
        self.q_size = size + 1
        self.arr = [float('inf')] * self.q_size
        self.head = 0
        self.tail = 0
    
    def is_empty(self):
        return self.head - self.tail == 0

    def enque(self, elem):
        if self.head >= self.q_size:
            raise RuntimeError("Queue is full")
        self.arr[self.head] = elem
        self.head += 1

    def deque(self):
        if self.is_empty():
            raise RuntimeError("Empty Queue")
        elem = self.arr[self.tail] 
        self.arr[self.tail] = float('inf') 
        self.tail += 1
        return elem
    
    def peek(self):
        if self.is_empty():
            raise RuntimeError("Empty Queue")
        
    def print_que(self):
        print(self.arr[self.tail : self.head])


if __name__ == "__main__":
    que = Queue(5)
    que.enque(12)
    que.enque(-2)
    que.enque(2)
    que.print_que()
    que.enque(1)
    que.print_que()
    que.deque()
    que.print_que()
    que.enque(-3)
    que.print_que()
    que.enque(4)
    que.enque(-9)

