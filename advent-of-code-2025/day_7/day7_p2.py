def dfs(mat, i, j, memo):
    if (i, j) in memo:
        return memo[(i, j)]

    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]):
        return 0

    if mat[i][j] != ".":
        return 0

    if i == len(mat) - 1:
        return 1

    if mat[i + 1][j] == "^":
        left = dfs(mat, i + 1, j - 1, memo)
        right = dfs(mat, i + 1, j + 1, memo)
        return left + right

    mat[i][j] = "|"
    val = dfs(mat, i + 1, j, memo)
    mat[i][j] = "."

    memo[(i, j)] = val
    return val


def emulate(mat):
    source = mat[0].index("S")
    memo = {}

    count = dfs(mat, 1, source, memo)
    return count


if __name__ == "__main__":
    with open("day7.txt") as f:
        mat = f.read().strip().split("\n")

    mat = [list(row) for row in mat]

    count = emulate(mat)
    print(count)
