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
        while curr < self.size:
            if self.elems[curr] == val:
                return True
            elif self.elems[curr] > val:
                curr = 2 * curr + 1
            else:
                curr = 2 * curr + 2
        return False

        

if __name__ == "__main__":
    bst = BST(6)
    bst.insert(4)
    bst.insert(2)
    bst.insert(1)
    bst.insert(10)
    bst.insert(3)
    bst.insert(6)
    bst.insert(12)
    print(bst.elems)
    print(bst.find(1))
    print(bst.find(23))