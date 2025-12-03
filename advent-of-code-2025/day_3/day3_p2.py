def best_12(s: str) -> str:
    stack = []
    to_pick = 12

    for i, ch in enumerate(s):
        remain = len(s) - i

        while stack and stack[-1] < ch and (len(stack) - 1 + remain >= to_pick):
            stack.pop()

        stack.append(ch)

        if len(stack) > to_pick:
            stack.pop()

    return "".join(stack[:12])


if __name__ == "__main__":
    with open("day3.txt") as f:
        lines = f.readlines()

    ans = 0
    for line in lines:
        line = line.strip()
        best = best_12(line)
        print(f"Best for line {line} is {best}")
        ans += int(best)

    print(ans)
