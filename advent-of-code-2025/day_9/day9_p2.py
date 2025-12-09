from shapely.geometry import Point, Polygon


def create_rectangle(p1, p2):
    return Polygon([p1, (p2[0], p1[1]), p2, (p1[0], p2[1])])


def area(x1, y1, x2, y2):
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)


if __name__ == "__main__":
    pos = [
        list(map(int, line.strip().split(","))) for line in open("day9.txt").readlines()
    ]

    polygon = Polygon(pos)
    ans = 0

    for first in pos:
        for second in pos:
            rect = create_rectangle(first, second)
            if polygon.contains(rect):
                ans = max(ans, area(first[0], first[1], second[0], second[1]))

    print(ans)
