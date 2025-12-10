import regex as re
from z3 import Optimize, Int, Sum, sat

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
            
            # Z3 Optimization
            opt = Optimize()
            
            button_vars = [Int(f'btn_{i}') for i in range(len(buttons))]
            
            for var in button_vars:
                opt.add(var >= 0)
                
            for i, jol in enumerate(joltage):
                s = [button_vars[j] for j, btn in enumerate(buttons) if i in btn]
                opt.add(Sum(s) == jol)
                
            opt.minimize(Sum(button_vars))
            
            if opt.check() == sat:
                model = opt.model()
                res = sum(model[var].as_long() for var in button_vars)
            else:
                raise ValueError("No solution found")

            ans += res


    print(ans)