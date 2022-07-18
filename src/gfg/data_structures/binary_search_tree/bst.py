# from binary_tree.binary_tree import inorder_iterative


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.num_nodes = 0
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            prev, curr = None, self.root
            while curr:
                prev = curr
                if curr.data == data:
                    # BST can not have duplicate keys
                    print("Insert operation cancelled. BST can't have duplicate keys.")
                    return -1
                elif curr.data > data:
                    curr = curr.left
                else:
                    curr = curr.right
            if prev:
                if prev.data > data:
                    prev.left = TreeNode(data)
                else:
                    prev.right = TreeNode(data)
        print(f"Inserted {data}.")
        self.num_nodes += 1
        return 0

    def delete_node(self, root, X):
        if not root:
            return None
        if root.data > X:
            root.left = self.delete_node(root.left, X)
        elif root.data < X:
            root.right = self.delete_node(root.right, X)
        else:
            # X has been found
            if not root.left:
                right_child = root.right
                del root
                return right_child
            elif not root.right:
                left_child = root.left
                del root
                return left_child
            else:
                successor = self.dig_left(root.right)
                root.data = successor.data
                root.right = self.delete_node(root.right, successor.data)
        return root

    def dig_left(self, root):
        while root.left:
            root = root.left
        return root

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)
                

if __name__ == "__main__":
    bst = BST()
    bst.insert(10)
    bst.insert(8)
    bst.insert(8)
    bst.insert(12)
    bst.insert(20)
    bst.inorder(bst.root)
