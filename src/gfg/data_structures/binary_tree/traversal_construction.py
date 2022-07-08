import time


pre_index = 0

def printPostOrder(inorder, preorder, n):
    # Code here
    res = []
    printPostOrderUtil(inorder, preorder, 0, n - 1, res)
    # for elem in res:
        # print(elem, sep=" ")
    print(res)
    

def printPostOrderUtil(inorder, preorder, in_start, in_end, res):
    global pre_index
    if in_start > in_end:
        return
    root_index = search(inorder, in_start, in_end, preorder[pre_index])
    pre_index += 1
    printPostOrderUtil(inorder, preorder, in_start, root_index - 1, res)
    printPostOrderUtil(inorder, preorder, root_index + 1, in_end, res)
    res.append(inorder[root_index])


def search(inorder, in_start, in_end, data):
    for i in range(in_start, in_end + 1, 1):
        if inorder[i] == data:
            return i
    return i


def num_trees_inorder(inorder, start, end):
    if start >= end:
        return 1
    res = 0
    for i in range(start, end + 1, 1):
        left = num_trees_inorder(inorder, start, i - 1)
        right = num_trees_inorder(inorder, i + 1, end)
        res += (left * right)
    return res


def num_trees_inorder_dp(inorder, start, end):
    n = end - start + 1
    catalan = [0] * (n + 1)
    catalan[0], catalan[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    return catalan[n]


if __name__ == "__main__":
    # inorder = [4, 2, 5, 1, 3, 6]
    # preorder = [1, 2, 4, 5, 3, 6]
    # inorder = [1, 2, 4, 5, 6, 8, 7] 
    # preorder = [1, 2, 4, 5, 6, 7, 8] 
    inorder = [10, 1, 30, 40, 20]
    preorder = [1, 10, 20, 30, 40]
    printPostOrder(inorder, preorder, len(inorder))
    inorder = [4, 5, 7, 6, 53, 4, 56, 76, 1, 23, 50, 62, 100, 101, 72]
    prev = time.time()
    print(num_trees_inorder(inorder, 0, len(inorder)-1))
    print(time.time() - prev)
    prev = time.time()
    print(num_trees_inorder_dp(inorder, 0, len(inorder)-1))
    print(time.time() - prev)
