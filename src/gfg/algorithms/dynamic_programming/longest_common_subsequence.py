def lcs(s1: str, s2: str, n1: int, n2: int) -> int:
    table = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    return table[n1][n2]

def lc_substr(s1: str, s2: str, n1: int, n2: int) -> int:
    table = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    max_substr = 0
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
                max_substr = max(max_substr, table[i][j])
            else:
                table[i][j] = 0
    return max_substr 

def print_lcs(s1: str, s2: str, n1: int, n2: int) -> str:
    table = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = 1 + table[i - 1][j - 1]
            else:
                table[i][j] = max(table[i - 1][j], table[i][j - 1])
    result_list = []
    print_lcs_util(table, s1, s2, n1, n2, "", result_list)
    result_list = sorted(set(result_list))
    return result_list
    # i, j = n1, n2
    # while i > 0 and j > 0:
    #     if s1[i - 1] == s2[j - 1]:
    #         result += s1[i - 1]
    #         i -= 1
    #         j -= 1
    #     else:
    #         if table[i - 1][j] > table[i][j - 1]:
    #             i -= 1
    #         else:
    #             j -= 1
    # return result[::-1]

def print_lcs_util(table, s1, s2, n1, n2, result, res_list):
    if n1 <= 0 or n2 <= 0:
        res_list.append(result[::-1])
        return
    if s1[n1 - 1] == s2[n2 - 1]:
        result += s1[n1 - 1]
        print_lcs_util(table, s1, s2, n1 - 1, n2 - 1, result, res_list)
    else:
        if table[n1 - 1][n2] > table[n1][n2 - 1]:
            print_lcs_util(table, s1, s2, n1 - 1, n2, result, res_list)
        elif table[n1][n2 - 1] > table[n1 - 1][n2]:
            print_lcs_util(table, s1, s2, n1, n2 - 1, result, res_list)
        else:
            print_lcs_util(table, s1, s2, n1 - 1, n2, result, res_list)
            print_lcs_util(table, s1, s2, n1, n2 - 1, result, res_list)


if __name__ == "__main__":
    s1 = "abaaa"
    s2 = "baabaca"
    n1, n2 = len(s1), len(s2)
    print(lcs(s1, s2, n1, n2))
    print(lc_substr(s1, s2, n1, n2))
    print(print_lcs(s1, s2, n1, n2))