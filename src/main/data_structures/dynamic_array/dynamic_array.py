class DynamicArray:
    def __init__(self, size):
        self.size = size
        self.arr = [None] * size
        self.curr_index = 0
    
    def insert(self, val):
        if self.curr_index >= self.size:
            self.arr += [None] * self.size
            self.size = len(self.arr)
        self.arr[self.curr_index] = val
        self.curr_index += 1
    
    def remove(self, val):
        index = self.get_index(val)
        if index == -1:
            return False
        for i in range(index + 1, self.size, 1):
            self.arr[i - 1] = self.arr[i]
        self.arr[self.size - 1] = None
        self.size -= 1
        self.curr_index -= 1
        return True

    def get_index(self, val):
        for i, elem in enumerate(self.arr):
            if elem == val:
                return i
        return -1

    def print_array(self):
        print(self.arr)


if __name__ == "__main__":
    da = DynamicArray(3)
    da.insert(3)
    da.insert(0)
    da.insert(8)
    da.insert(4)
    da.print_array()
    da.remove(3)
    da.print_array()
    print(da.curr_index)
    da.insert(67)
    da.print_array()
    da.insert(6)
    da.print_array()
    print(da.curr_index, da.size)
    da.insert(7)
    da.print_array()

