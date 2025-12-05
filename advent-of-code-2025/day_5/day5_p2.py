import regex as re

if __name__ == "__main__":
    pattern = r"(\d+)-(\d+)"
    fresh_ranges = []

    with open("day5.txt", "r") as f:
        while line := f.readline().strip():
            head, tail = re.match(pattern, line).groups()
            fresh_ranges.append((int(head), int(tail)))

    fresh_ranges.sort(key=lambda x: x[0])

    merged_ranges = []
    while fresh_ranges:
        current_range = fresh_ranges.pop(0)

        while fresh_ranges and fresh_ranges[0][0] <= current_range[1]:
            next_range = fresh_ranges.pop(0)
            current_range = (current_range[0], max(current_range[1], next_range[1]))

        merged_ranges.append(current_range)

    ans = 0
    for r in merged_ranges:
        ans += r[1] - r[0] + 1

    print(ans)
