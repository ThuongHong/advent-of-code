if __name__ == "__main__":
    with open("day3.txt") as f:
        lines = f.readlines()

    ans = 0
    for line in lines:
        line = line.strip()
        max_joltage = 0
        for i in range(len(line)):
            first, second = line[i], max(line[i + 1 :], default="")
            max_joltage = max(max_joltage, int(first + second))
        ans += max_joltage

    print(ans)
