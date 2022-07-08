from binary_tree import inorder_iterative, TreeNode


def replace_node_with_sum(root, pprev, prev, curr):
    if not root:
        return
    replace_node_with_sum(root.left, pprev, prev, curr)
    pprev = prev
    prev = curr
    curr = root
    print(curr.data)
    if pprev:
        prev.data = curr.data + pprev.data
    else:
        prev.data = curr.data
    replace_node_with_sum(root.right, pprev, prev, curr)


curr, prev = None, None
def replace_in_successor(root):
    global curr, prev
    if not root:
        return
    replace_in_successor(root.left)
    prev = curr
    curr = root
    if prev:
        prev.next = curr
        if not curr.left and not curr.right:
            curr.next = TreeNode(-1)
    replace_in_successor(root.right)


def find_inorder_successor(root, key, result):
    global prev, curr
    if not root:
        return
    find_inorder_successor(root.left, key, result)
    prev = curr
    curr = root
    if prev and prev.data == key:
        result.append(curr.data)
    find_inorder_successor(root.right, key, result)


def print_in_successor(root):
    if not root:
        return
    print_in_successor(root.left)
    print(root.data)
    print(root.next.data)
    print_in_successor(root.right)

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(8)
    root.left.left = TreeNode(3)
    root.right = TreeNode(12)
    print(inorder_iterative(root))
    # replace_in_successor(root)
    res = []
    find_inorder_successor(root, 3, res)
    print(res)
    # print_in_successor(root)