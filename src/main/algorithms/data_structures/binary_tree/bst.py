from multiprocessing.sharedctypes import Value


class BST:
    def __init__(self, size):
        self.size = size
        self.elems = [None] * size

    # Insert a value into the BST
    def insert(self, val):
        curr = 0
        while curr < self.size:
            if curr < self.size and self.elems[curr] == None:
                self.elems[curr] = val
                return 0 
            if self.elems[curr] > val:
                curr = 2 * curr + 1
            elif self.elems[curr] < val:
                curr = 2 * curr + 2
            else:
               print("Duplicate values are not allowed") 
               return -1
        print("BST is full")

    # Find a value into the BST
    def find(self, val):
        curr = 0
        while curr < self.size and self.elems[curr]:
            if self.elems[curr] == val:
                return curr
            elif self.elems[curr] > val:
                curr = 2 * curr + 1
            else:
                curr = 2 * curr + 2
        return -1
    
    def successor(self, node):
        index = self.find(node)
        if index == -1:
            raise ValueError("Node does not exist in the tree")
        left = 2 * index + 1
        right = 2 * index + 2
        left_succ, right_succ = None, None
        while left < self.size and self.elems[left]:
            left_succ = self.elems[left]
            left = 2 * left + 2
        while right < self.size and self.elems[right]:
            right_succ = self.elems[right]
            right = 2 * right + 1
        return left_succ if left_succ else right_succ


if __name__ == "__main__":
    bst = BST(20)
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(10)
    bst.insert(3)
    bst.insert(6)
    bst.insert(5)
    print(bst.elems)
    print(bst.find(1))
    print(bst.find(23))
    print(bst.find(2))
    print(bst.successor(10))