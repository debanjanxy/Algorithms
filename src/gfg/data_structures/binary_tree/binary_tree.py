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

def print_tree(root):
    if not root:
        return
    que = deque([root])
    while que:
        curr = que.popleft()
        print(curr.data)
        if curr.left:
            que.append(curr.left)
        if curr.right:
            que.append(curr.right)
    print('-' * 127)

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

