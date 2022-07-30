from collections import deque
# import os, sys
# sys.path.insert(0, os.path.abspath("../binary_tre"))
# from binary_tree import binary_tree
# from binary_tree.binary_tree import inorder_iterative


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class NodeRange:
    def __init__(self, **kwargs):
        self.node = kwargs.get('node', None)
        self.min = kwargs.get('min_val', float("-inf"))
        self.max = kwargs.get('max_val', float("inf"))


def construct_bst_from_levelorder(levelorder):
    n = len(levelorder)
    i = 1
    root_node = TreeNode(levelorder[0])
    root_nr = NodeRange(node=root_node)
    que = deque([root_nr])
    while que:
        curr = que.popleft()
        parent = curr.node
        min_val, max_val = curr.min, curr.max
        if i < n and levelorder[i] < parent.data and levelorder[i] > min_val:
            parent.left = TreeNode(levelorder[i])
            que.append(NodeRange(node=parent.left, min_val=min_val, max_val=parent.data))
            i += 1
        if i < n and levelorder[i] > parent.data and levelorder[i] < max_val:
            parent.right = TreeNode(levelorder[i])
            que.append(NodeRange(node=parent.right, min_val=parent.data, max_val=max_val))
            i += 1
    return root_node


def copy(arr, n):
    root = TreeNode(arr[0])
    q = deque([])
    q.append(NodeRange(node=root))
    i = 1
    while q:
        curr = q.popleft()
        parent = curr.node
        min_val = curr.min
        max_val = curr.max
        if (i < n and min_val < arr[i] and arr[i] < parent.data):
            parent.left = TreeNode(arr[i])
            i += 1
            q.append(NodeRange(node=parent.left, min_val=min_val, max_val=parent.data))
        if (i < n and parent.data < arr[i] and arr[i] < max_val):
            parent.right = TreeNode(arr[i])
            i += 1
            q.append(NodeRange(node=parent.right, min_val=parent.data, max_val=max_val))
    return root


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data)
    inorder(root.right)


if __name__ == "__main__":
    lo = [7, 4, 12, 3]
    root = construct_bst_from_levelorder(lo)
    inorder(root)
    print('-' * 127)
    cp = copy(lo, len(lo))
    inorder(cp)

