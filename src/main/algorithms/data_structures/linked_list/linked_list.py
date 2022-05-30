
class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self):
        trav = self.head
        while trav:
            next = trav.next
            trav.prev = trav.next = None
            trav.data = None
            trav = next
        self.head = self.tail = trav = None    
        self.size = 0
    
    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_last(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.tail.next = Node(elem, self.tail, None)
            self.tail = self.tail.next
        self.size += 1

    def add_front(self, elem):
        if self.is_empty():
            self.head = self.tail = Node(elem, None, None)
        else:
            self.head.prev = Node(elem, None, self.head)
            self.head = self.head.prev 
        self.size += 1

    def peek_first(self):
        if self.is_empty():
            raise RuntimeError("Empty List")
        return self.head.data 

    def peek_last(self):
        if self.is_empty():
            raise RuntimeError("Empty List")
        return self.tail.data

    def remove_first(self):
        if self.is_empty():
            raise RuntimeError("Empty List")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        if self.is_empty():
            self.tail = None
        else:
            self.head.prev = None
        return data 

    def remove_last(self):
        if self.is_empty():
            raise RuntimeError("Empty List")
        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1
        if self.is_empty():
            self.head = None
        else:
            self.tail.next = None
        return data 

    def remove(self, node):
        if node.prev == None:
            self.remove_first()
        if node.next == None:
            self.remove_last()
        node.prev.next = node.next
        node.next.prev = node.prev
        data = node.data
        node.data = node.next = node.prev = None
        size -= 1
        return data

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise ValueError("Index is out of range")
        if index < self.size / 2:
            curr = self.head
            for i in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for i in range(index):
                curr = curr.prev
        return curr.data

    def remove_value(self, value):
        curr = self.head
        while curr:
            if curr.data == value:
                self.remove(curr)
                return True
            curr = curr.next
        return False

    def index_of(self, value):
        index = 0
        curr = self.head
        while curr:
            if curr.data == value:
                return index
            curr = curr.next
            index += 1
        return -1

    def contains(self, value):
        return self.index_of(value) != -1

    def to_string(self):
        curr = self.head
        result = ""
        while curr:
            result += str(curr.data) + " "
            curr = curr.next
        return result


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.add_front(2)
    dll.add_front(3)
    dll.add_last(5)
    print(dll.to_string())
    print(dll.remove_first())
    print(dll.remove_last())
    print(dll.remove_at(0))
    print(dll.remove_value(2)) # should throw a RunTimeError
