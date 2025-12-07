def emulate(mat):
    source = mat[0].index("S")
    mat[1][source] = "|"

    count = 0

    for i in range(1, len(mat) - 1):
        for j in range(len(mat[0])):
            if mat[i][j] == "|":
                if mat[i + 1][j] == "^":
                    mat[i + 1][j - 1] = "|"
                    mat[i + 1][j + 1] = "|"
                    count += 1
                else:
                    mat[i + 1][j] = "|"

    return count


if __name__ == "__main__":
    with open("day7.txt") as f:
        mat = f.read().strip().split("\n")

    mat = [list(row) for row in mat]

    with open("test.txt", "w") as f:
        count = emulate(mat)
        print(count)
        for row in mat:
            f.write("".join(row) + "\n")
