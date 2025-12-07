import numpy as np


def apply_operation(operands, i, operator):
    res = int(operands[0][i])

    for operand in operands[1:]:
        if operator == "+":
            res += int(operand[i])
        elif operator == "*":
            res *= int(operand[i])

    return res


if __name__ == "__main__":
    data = np.loadtxt("day6.txt", dtype=str).tolist()

    operands = data[:-1]
    operators = data[-1]

    total = 0
    for i, op in enumerate(operators):
        total += apply_operation(operands, i, op)

    print(total)
