import regex as re

if __name__ == "__main__":
    pattern = r"(\d+)-(\d+)"
    preprocess_phase = True
    fresh_ranges = []
    ans = 0

    with open("day5.txt", "r") as f:
        while line := f.readline():
            line = line.strip()

            if not line:
                preprocess_phase = False
                continue

            if preprocess_phase:
                head, tail = re.match(pattern, line).groups()
                fresh_ranges.append((int(head), int(tail)))
            else:
                ingredient_id = int(line)
                for r in fresh_ranges:
                    if r[0] <= ingredient_id <= r[1]:
                        ans += 1
                        break

    print(ans)
