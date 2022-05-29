from linked_list.linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def push(self, elem):
        self.dll.add_front(elem)

    def pop(self):
        if self.is_empty():
            raise RuntimeError("Empty Stack")
        pop_elem = self.dll.remove_first()
        return pop_elem

    def is_empty(self):
        return self.dll.is_empty()

    def peek(self):
        if self.is_empty():
            raise RuntimeError("Empty Stack")
        return self.dll.head.data

    def size(self):
        return self.dll.size


    
if __name__ == "__main__":
    st = Stack()
    st.push(2)
    st.push(3)
    st.push(1)
    st.push(5)
    print(st.pop())
    print(st.pop())