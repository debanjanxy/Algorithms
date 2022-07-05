from curses.ascii import isalnum
from binary_tree import TreeNode, print_tree


def eval_tree(root):
    if root:
        if is_operand(root.data):
            return root.data
        else:
            a = eval_tree(root.left)
            b = eval_tree(root.right)
            return calculate(a, b, root.data)

def is_operand(val):
    return isalnum(val)

def calculate(a, b, op):
    return eval(f"{a} {op} {b}")


if __name__ == "__main__":
    root = TreeNode("+")
    root.left = TreeNode("3")
    root.right = TreeNode("*")
    root.right.left = TreeNode("+")
    root.right.right = TreeNode("2")
    root.right.left.left= TreeNode("5")
    root.right.left.right= TreeNode("9")
    print_tree(root)
    print(eval_tree(root))
