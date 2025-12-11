from importlib.resources import path
import regex as re


def dfs(node, adj, memo, dac=False, fft=False):
    if node == 'out':
        return 1 if dac and fft else 0
    elif node == 'dac':
        dac = True
    elif node == 'fft':
        fft = True

    key = (node, dac, fft)
    if key not in memo:
        cnt = 0

        for neighbor in adj.get(node, []):
            cnt += dfs(neighbor, adj, memo, dac, fft)

        memo[key] = cnt

    return memo[key]


if __name__ == "__main__":
    with open("day11.txt") as f:
        lines = f.readlines()

    pattern = r'([a-z]{3}):\s*(\S+(?:\s+\S+)*)$'
    matches = []
    for line in lines:
        match = re.match(pattern, line)
        if match:
            head = match.group(1)
            tail = match.group(2).strip().split()
            matches.append((head, tail))

    adj = {}
    for head, tail in matches:
        adj[head] = tail

    print(f'Part 1: {dfs("you", adj, {}, True, True)}')
    print(f'Part 2: {dfs("svr", adj, {}, False, False)}')
    