import regex as re


def split_into_parts(num_str: str, part_size: int):
    return [num_str[i : i + part_size] for i in range(0, len(num_str), part_size)]


def isInvalid(num: int):
    num = str(num)
    for partition in range(2, len(num) + 1):
        s = set()
        part_size = len(num) // partition
        parts = split_into_parts(num, part_size)
        s.update(parts)
        if len(s) == 1:
            return True
    return False


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
