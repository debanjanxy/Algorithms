from curses.ascii import isalnum

from requests import post
from binary_tree import TreeNode, print_level_order, print_inorder, inorder_iterative


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

def construct_tree(postfix):
    stack = []
    root = None
    for ch in postfix:
        # ch is an operand
        if not is_operator(ch):
            stack.append(TreeNode(ch + " "))
        # ch is an operator
        else:
            root = TreeNode(ch + " ")
            root.right, root.left = stack.pop(), stack.pop()
            stack.append(root)
    return stack.pop()

def is_operator(c):
    if (c == '+' or c == '-' or c == '*' or c == '/' or c == '^'):
        return True
    return False


if __name__ == "__main__":
    root = TreeNode("+")
    root.left = TreeNode("3")
    root.right = TreeNode("*")
    root.right.left = TreeNode("+")
    root.right.right = TreeNode("2")
    root.right.left.left= TreeNode("5")
    root.right.left.right= TreeNode("9")
    print_level_order(root)
    print(eval_tree(root))
    postfix = "abc+*"
    print_inorder(construct_tree(postfix))
    print(inorder_iterative(construct_tree(postfix)))