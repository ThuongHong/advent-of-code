pos = [list(map(int, line.strip().split(","))) for line in open("day9.txt").readlines()]

ans = 0
for i in range(len(pos)):
    for j in range(i + 1, len(pos)):
        area = abs(pos[i][0] - pos[j][0] + 1) * abs(pos[i][1] - pos[j][1] + 1)
        ans = max(ans, area)

print(ans)
