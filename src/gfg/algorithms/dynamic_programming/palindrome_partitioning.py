def palindrome_partitioning(s):
    n = len(s)
    pal = [[False] * (n + 1) for _ in range(n + 1)]
    cut = [[-1] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        