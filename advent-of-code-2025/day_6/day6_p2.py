def check_column(lines, j):
    for line in lines:
        if line[j] != " ":
            return False
    return True


def apply_operator(lines, start, end, operator):
    nums = []
    for i in range(start, end):
        num = []

        for j in range(len(lines)):
            if lines[j][i] == " ":
                continue
            num.append(lines[j][i])

        if num:
            nums.append(int("".join(num).rstrip()))

    res = nums[0]
    print(nums)
    for num in nums[1:]:
        if operator == "+":
            res += num
        elif operator == "*":
            res *= num

    return res


if __name__ == "__main__":
    with open("day6.txt") as f:
        lines = f.read().strip().split("\n")

    operators = lines[-1].replace(" ", "")
    lines = lines[:-1]

    col_indices = [0]

    for j in range(len(lines[0])):
        if check_column(lines, j):
            col_indices.append(j)
    col_indices.append(len(lines[0]))

    total = 0
    for i, operator in enumerate(operators):
        start = col_indices[i]
        end = col_indices[i + 1]
        result = apply_operator(lines, start, end, operator)
        total += result
    print(total)
