from math import dist


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            if self.rank[rootA] > self.rank[rootB]:
                self.parent[rootB] = rootA
            elif self.rank[rootA] < self.rank[rootB]:
                self.parent[rootA] = rootB
            else:
                self.parent[rootB] = rootA
                self.rank[rootA] += 1
            return True
        return False


if __name__ == "__main__":
    junctions = [list(map(int, line.strip().split(","))) for line in open("day8.txt")]
    distances = [
        (i, j, dist(junctions[i], junctions[j]))
        for i in range(len(junctions))
        for j in range(i + 1, len(junctions))
    ]
    distances.sort(key=lambda x: x[2])

    dsu = DSU(len(junctions))
    for i, j, d in distances:
        dsu.union(i, j)
        roots = set(dsu.find(i) for i in range(len(junctions)))
        if len(roots) == 1:
            print(
                f"{junctions[i][0]} x {junctions[j][0]} = {junctions[i][0] * junctions[j][0]}"
            )
            break
