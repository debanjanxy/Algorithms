from collections import deque
from typing import List, Optional
from binary_tree import print_level_order


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def build_tree_in_pre(self, inorder: List[int], preorder: List[int]) -> Optional[TreeNode]:
        """
        Build tree from the given inorder and preorder traversals
        """
        self.length = len(preorder)
        self.pre_index = 0
        self.inorder_map = {elem : i for i, elem in enumerate(inorder)}
        return self.build_tree_in_pre_util(inorder, preorder, 0, self.length - 1)

    def build_tree_in_pre_util(self, inorder, preorder, start_in, end_in):
        if self.pre_index >= self.length or start_in > end_in:
            return None
        root = preorder[self.pre_index]
        self.pre_index += 1
        root_index = self.inorder_map[root]
        root_node = TreeNode(root)
        if start_in == end_in:
            return root_node
        root_node.left = self.build_tree_in_pre_util(inorder, preorder, start_in, root_index - 1)
        root_node.right = self.build_tree_in_pre_util(inorder, preorder, root_index + 1, end_in)
        return root_node


if __name__ == "__main__":
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(4)
    # root.left.right = TreeNode(3)
    # root.right = TreeNode(5)

    sol = Solution()
    inorder = [1, 6, 8, 7]
    preorder = [1, 6, 7, 8]
    root = sol.build_tree_in_pre(inorder, preorder)
    print_level_order(root)

