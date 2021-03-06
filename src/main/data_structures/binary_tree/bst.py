from collections import deque


class BSTNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.num_nodes = 0
        self.root = None
    
    def insert(self, val):
        node = BSTNode(val)
        if self.contains(self.root, val):
            return False
        else:
            self.root = self.__insert(self.root, val)
            self.num_nodes += 1
            return True
    
    # Private method
    def __insert(self, node, val):
        if not node:
            node = BSTNode(val)
        else:
            if node.data > val:
                node.left = self.__insert(node.left, val)
            else:
                node.right = self.__insert(node.right, val)
        return node

    def remove(self, val):
        if self.contains(self.root, val):
            self.root = self.__remove(self.root, val)
            self.num_nodes -= 1
            return True
        return False

    def __remove(self, node, val):
        # First check if the node is None
        if not node:
            return None
        # If val is smaller then search in the left-subtree
        if node.data > val:
            node.left = self.__remove(node.left, val)
        # If val is greater then search in the right-subtree
        elif node.data < val:
            node.right = self.__remove(node.right, val)
        # We've found the node
        else:
            # If the node doesn't have left child
            # We can just replace current node with it's right child
            if not node.left:
                right_child = node.right
                node.data = node.right = None
                return right_child
            # If the node doesn't have right child
            # We can just replace current node with it's left child
            elif not node.right:
                left_child = node.left 
                node.left = node.data = None
                return left_child
            # If we have both left and right children
            else:
                # We can get the successor of the current node from right subtree
                # Or from the left subtree
                tmp = self.dig_left(node.right) 
                # Replace current node's value with successor's value 
                node.data = tmp.data
                # Then just modify the right subtree by deleting the successor node
                node.right = self.__remove(node.right, tmp.data)
        return node

    def dig_left(self, node):
        while node.left:
            node = node.left
        return node

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if not node:
            return 0
        return 1 + max(self.__height(node.left), self.__height(node.right))

    def contains(self, node, val):
        if not node:
            return False
        if node.data == val:
            return True 
        elif node.data > val:
            return self.contains(node.left, val)
        else:
            return self.contains(node.right, val)
    
    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.num_nodes


    def traverse(self, order):
        if order == 'pre':
            return self.preorder(self.root)
        elif order == 'in':
            return self.inorder(self.root)
        elif order == 'level':
            return self.levelorder(self.root)
        else:
            return self.postorder(self.root)

    def preorder(self, node):
        stack = [node]
        while stack:
            curr = stack.pop()
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
            yield curr.data
    
    def inorder(self, node):
        stack, curr = [], node
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                yield curr.data
                curr = curr.right
                
    def postorder(self, node):
        stack = [node]
        res = []
        while stack:
            curr = stack.pop()
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            res.append(curr.data)
        while res:
            yield res.pop()


    def levelorder(self, node):
        que = deque([node])
        while que:
            curr = que.popleft()
            if curr:
                yield curr.data
                if curr.left:
                    que.append(curr.left)
                if curr.right:
                    que.append(curr.right)



if __name__ == "__main__":
    bst = BST()
    # Insertions and Deletions
    bst.insert(14)
    bst.insert(8)
    bst.insert(20)
    bst.insert(6)
    bst.insert(10)
    bst.insert(7)

    bst.remove(8)

    # Traversals
    traverse_res = bst.traverse('post')
    print([elem for elem in traverse_res])
