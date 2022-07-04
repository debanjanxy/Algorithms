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

def print_tree(root):
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

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(7)
    root.right = TreeNode(9)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(8)
    print_tree(root)
    root = insert_level_order(root, 12)
    print_tree(root)
    root = deletion(root, 10)
    print_tree(root)

