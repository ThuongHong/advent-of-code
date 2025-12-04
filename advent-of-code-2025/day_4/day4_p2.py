def check(mat, i, j):
    if mat[i][j] != "@":
        return False

    c = 0
    for row in range(i - 1, i + 2):
        if row < 0 or row >= len(mat):
            continue
        for col in range(j - 1, j + 2):
            if col < 0 or col >= len(mat[0]) or (col == j and row == i):
                continue

            if mat[row][col] == "@":
                c += 1

            if c >= 4:
                return False

    return True


def checkPause(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if check(mat, i, j):
                return False
    return True


if __name__ == "__main__":
    with open("day4.txt", "r") as f:
        mat = f.readlines()

    for i in range(len(mat)):
        mat[i] = mat[i].strip()

    ans = 0
    while not checkPause(mat):
        newMat = []
        for i in range(len(mat)):
            newRow = ""
            for j in range(len(mat[0])):
                if check(mat, i, j):
                    newRow += "."
                    ans += 1
                else:
                    newRow += mat[i][j]
            newMat.append(newRow)
        mat = newMat
        # ans += 1

    print(ans)

    # print(mat)
