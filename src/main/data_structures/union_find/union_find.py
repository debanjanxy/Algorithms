class UnionFind:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size <= 0 is not allowed")
        self.size = size
        self.component_sizes = []
        self.id = []
        self.num_components = size 
        for i in range(size):
            self.component_sizes.append(1)
            self.id.append(i)

    # Find which component/set, p belongs to
    def find(self, p):
        # Find the root of the component
        root = p
        while self.id[root] != root:
            root = self.id[root]
        # Point all the nodes in the path to the root node
        # This is known as path compression
        # This has constant amortized time complexity
        while root != p:
            next = self.id[p]
            self.id[p] = root
            p = next
        return root

    # Check if two nodes belongs to the same component
    def is_connected(self, p, q):
        return self.find(p) == self.find(q)

    # Return the size of the component that a node belongs to
    def component_size(self, p):
        return self.component_sizes[self.find(p)]

    # Return the no. of elements in the UnionFind data structure
    def size(self):
        return self.size

    # Return the no. of components in the UnionFind data structure
    def num_components(self):
        return self.num_components

    # Union two components p and q
    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        # If both belong to the same component then return
        if root_p == root_q:
            # If p and q are already in the same component then return -1
            return -1
        # Merge the bigger component with the smaller one
        if self.component_size(p) >= self.component_size(q):
            self.component_sizes[root_p] += self.component_sizes[root_q]
            self.id[root_q] = root_p 
        else:
            self.component_sizes[root_q] += self.component_sizes[root_p]
            self.id[root_p] = root_q
        # By performing union once, the no. of components will decrease by 1
        self.num_components -= 1
        # If both the nodes are united then return 0
        return 0


if __name__ == "__main__":
    uf = UnionFind(6)
    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)
    print(uf.is_connected(3, 5))
    print(uf.find(2))
    print(uf.find(5))
    uf.union(2, 5)
    print(uf.find(5))
    print(uf.find(0))
    print(uf.find(4))

        
        







    

