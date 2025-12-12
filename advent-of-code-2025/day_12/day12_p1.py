import regex as re

if __name__ == "__main__":
    with open("day12.txt") as f:
        lines = f.read().split("\n")
        
    shapes = []
    area = 0
    shape = []
    i = 0
    while True:
        if not lines[i]:
            i += 1
            shapes.append((shape[1:], area))
            area = 0
            shape = []
            continue

        if len(shapes) > 5:
            lines = lines[i:]
            break
        
        shape.append(lines[i])
        area += lines[i].count("#")
        i += 1

    pattern = r'(\d+)x(\d+): (.+)'
    regions = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            # (width, height, [presents])
            a, b, c = match.groups()
            c = [int(x) for x in c.split(" ")]
            regions.append((int(a), int(b), c))
            
    # Solve
    ans = 0
    for region in regions:
        width, height, presents = region
        demanded_area = sum(shapes[i][1] * present for i, present in enumerate(presents))
        ans += demanded_area <= width * height

    print(f"Total fully covered regions: {ans}")
