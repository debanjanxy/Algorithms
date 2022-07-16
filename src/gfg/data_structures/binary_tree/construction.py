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

    def construct_tree_maxheap_inorder(self, inorder):
        """
        Construct tree from the inorder traversal of a max heap
        """
        n = len(inorder)
        return self.construct_tree_maxheap_inorder_util(inorder, 0, n - 1)

    def construct_tree_maxheap_inorder_util(self, inorder, start, end):
        if start > end:
            return None
        root_index = self.get_max_index(inorder, start, end)
        root_node = TreeNode(inorder[root_index])
        if start == end:
            return root_node
        root_node.left = self.construct_tree_maxheap_inorder_util(inorder, start, root_index - 1)
        root_node.right= self.construct_tree_maxheap_inorder_util(inorder, root_index + 1, end)
        return root_node


    def get_max_index(self, arr, start, end):
        curr_max = float("-inf") 
        max_index = None
        for i in range(start, end + 1, 1):
            elem = arr[i]
            if elem > curr_max:
                curr_max = elem
                max_index = i
        return max_index


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
    inorder = [6, 8, 5, 10, 3, 7, 2]
    root = sol.construct_tree_maxheap_inorder(inorder)
    print_level_order(root)

