import regex as re
from collections import deque

def bfs(diagram, buttons, target, start_pos):
    # (position in diagram, num of moves, state)
    initial_state = (start_pos, 0, tuple(0 for _ in diagram))
    queue = deque([initial_state])
    visited = set()
    visited.add(initial_state)

    while queue:
        pos, moves, state = queue.popleft()

        if list(state) == target:
            return moves

        for i, button in enumerate(buttons):
            new_joltage = list(state)
            for idx in button:
                new_joltage[idx] = 1 - new_joltage[idx]

            new_state = (pos + 1, moves + 1, tuple(new_joltage))
            if new_state not in visited:
                visited.add(new_state)
                queue.append(new_state)

    return None

if __name__ == "__main__":
    with open("day10.txt", "r") as f:
        lines = f.read().splitlines()

    pattern = re.compile(r'^\s*\[([.#]+)\]\s*((?:\(\s*\d+(?:\s*,\s*\d+)*\s*\)\s*)*)\{\s*(\d+(?:\s*,\s*\d+)*)\s*\}\s*$')   
     
     
    ans = 0
    for line in lines:
        match = pattern.match(line)
        if match:
            diagram_str = match.group(1)
            buttons_str = match.group(2)
            joltage_str = match.group(3)

            diagram = [list(row) for row in diagram_str.split()][0]
            buttons = [tuple(map(int, t.strip('()').split(','))) for t in re.findall(r'\(\s*\d+(?:\s*,\s*\d+)*\s*\)', buttons_str)]
            joltage = list(map(int, joltage_str.split(',')))

            target = [1 if diagram[i] == '#' else 0 for i in range(len(diagram))]
            
            res = float('inf')
            for i, button in enumerate(buttons):
                tmp = bfs(diagram, buttons, target, i)
                if tmp is not None:
                    res = min(res, tmp)
            
            ans += res


    print(ans)