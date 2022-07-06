from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert_level_order(root, key):
    if not root:
        return TreeNode(key)
    que = deque([root])
    while que:
        curr = que.popleft()
        if not curr.left:
            curr.left = TreeNode(key) 
            return root
        elif not curr.right:
            curr.right = TreeNode(key)
            return root
        else:
            que.append(curr.left)
            que.append(curr.right)

def deletion(root, key):
    '''
    root: root of tree
    key:  key to be deleted
    return: root after deleting 
    '''
    parent, curr_parent = None, None
    que = deque([root])
    while que:
        curr = que.popleft()
        if curr.data == key:
            key_node = curr
        if curr.left:
            curr_parent = curr
            que.append(curr.left)
        if curr.right:
            curr_parent = curr
            que.append(curr.right)
    if key_node:
        key_node.data = curr.data
        if curr_parent.left == curr:
            curr_parent.left = None
        elif curr_parent.right == curr:
            curr_parent.right = None
        del curr
    return root

def print_level_order(root):
    if not root:
        return
    que = deque([root])
    result = []
    while que:
        curr = que.popleft()
        result.append(curr.data)
        if curr.left:
            que.append(curr.left)
        if curr.right:
            que.append(curr.right)
    print(result)

def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.data, sep=" ")
    print_inorder(root.right)

def is_continuous_tree(root):
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.left:
            if abs(curr.data - curr.left.data) != 1:
                return False
            stack.append(curr.left)
        if curr.right:
            if abs(curr.data - curr.right.data) != 1:
                return False
            stack.append(curr.right)
    return True



if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(12)
    root.right = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(8)
    print_level_order(root)
    print(is_continuous_tree(root))
    root = insert_level_order(root, 12)
    print_level_order(root)
    root = deletion(root, 10)
    print_level_order(root)
    print(is_continuous_tree(root))
