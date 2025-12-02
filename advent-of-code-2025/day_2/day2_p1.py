import regex as re


def isInvalid(num: int):
    num = str(num)
    mid = len(num) // 2
    return num[:mid] == num[mid:]


if __name__ == "__main__":
    with open("day2.txt", "r") as f:
        data = f.read()

    pattern = r"(\d+)-(\d+)"
    matches = re.findall(pattern, data)

    ans = 0
    for match in matches:
        first, last = match
        for i in range(int(first), int(last) + 1):
            if isInvalid(i):
                print(f"Invalid: {i}")
                ans += i

    print(f"Answer: {ans}")
