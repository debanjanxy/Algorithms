from collections import deque, defaultdict
from os import preadv


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None


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


def is_foldable(root):
    if not root:
        return True
    return is_foldable_util(root.left, root.right)


def is_foldable_util(n1, n2):
    if not n1 and not n2:
        return True
    elif (not n1 and n2) or (n1 and not n2):
        return False
    else:
        return is_foldable_util(n1.left, n2.right) and is_foldable_util(n1.right, n2.left)
    

def is_symmetric(root):
    if not root:
        return True
    return is_symmetric_util(root.left, root.right)


def is_symmetric_util(n1, n2):
    if not n1 and not n2:
        return True
    elif (not n1 and n2) or (n1 and not n2):
        return False
    else:
        return n1.data == n2.data and is_foldable_util(n1.left, n2.right) and is_foldable_util(n1.right, n2.left)


def inorder_iterative(root):
    result = []
    curr = root
    stack = []
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.data)
        curr = curr.right
    return result


def morris_inorder_traversal(root):
    curr = root
    while curr:
        if not curr.left:
            yield curr.data
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if not pre.right:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                yield curr.data
                curr = curr.right


def preorder_iterative(root):
    stack, res = [root], []
    while stack:
        curr = stack.pop()
        res.append(curr.data)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return res


def morris_preorder_traversal(root):
    curr, res = root, []
    while curr:
        if not curr.left:
            res.append(curr.data)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right and pre.right != curr:
                pre = pre.right
            if pre.right == curr:
                pre.right = None
                curr = curr.right
            else: 
                res.append(curr.data)
                pre.right = curr
                curr = curr.left
    return res


def spiral_level_order(root):
    que = deque([root, None])
    res, temp, i = [], [], 0
    while que:
        curr = que.popleft()
        if curr:
            temp.append(curr.data)
            if curr.left:
                que.append(curr.left)
            if curr.right:
                que.append(curr.right)
        else:
            if que:
                que.append(None)
            if i % 2 == 0:
                temp.reverse()
            res += temp
            temp = []
            i += 1
    return res


def print_boundary_view(root):
    if root:
        res = [root.data]
        print_left_view(root.left, res)
        print_leaves(root.left, res)
        print_leaves(root.right, res)
        print_right_view(root.right, res)
        return res


def print_left_view(root, res):
    if root:
        if root.left:
            res.append(root.data)
            print_left_view(root.left, res)
        elif root.right:
            res.append(root.data)
            print_left_view(root.right, res)


def print_right_view(root, res):
    if root:
        if root.right:
            print_right_view(root.right, res)
            res.append(root.data)
        elif root.left:
            print_right_view(root.left, res)
            res.append(root.data)


def print_leaves(root, res):
    if root:
        print_leaves(root.left, res)
        if not root.left and not root.right:
            res.append(root.data)
        print_leaves(root.right, res)


def level_order_recursive(root, level, res_map):
    if not root:
        return
    res_map[level].append(root.data)
    level_order_recursive(root.left, level + 1, res_map)
    level_order_recursive(root.right, level + 1, res_map)


def top_view(root):
    if not root:
        return []
    table = {}
    que = deque([(root, 0)])
    while que:
        curr_node, hdist = que.popleft()
        if hdist not in table:
            table[hdist] = curr_node.data
        if curr_node.left:
            que.append((curr_node.left, hdist - 1))
        if curr_node.right:
            que.append((curr_node.right, hdist + 1))
    result = []
    for hdist in sorted(table):
        result.append(table[hdist])
    return result


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

    # print(is_continuous_tree(root))

    # print(inorder_iterative(root))
    # print([node for node in morris_inorder_traversal(root)])

    # print(preorder_iterative(root))
    # print(morris_preorder_traversal(root))

    print(spiral_level_order(root))
    print(print_boundary_view(root))

    res_map = defaultdict(list)
    level_order_recursive(root, 0, res_map)
    print(res_map)