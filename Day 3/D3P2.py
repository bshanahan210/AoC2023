import re
from collections import defaultdict

# read data and initialize answer variable along with an adjacent variable
lines = open("C:\\Users\\Brendan\\AoC2023\\Day 3\\input3.txt").read().splitlines()
adj = defaultdict(list)  # defaultdict to store adjacent numbers for each gear
ans = 0

# same setup as part 1
for i, line in enumerate(lines):
    for m in re.finditer(r"\d+", line):
        idxs = [
            (i, m.start() - 1),  # left
            (i, m.end()),        # right
        ]
        idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
        idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
        
        # check for the gears in each line
        for a, b in idxs:
            if 0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] == "*":  # asterisk nearby within bounds
                adj[a, b].append(m.group())  # add the digit to the list of adjacent numbers for the current gear

# iterate through the adjacent numbers for each gear
for v in adj.values():
    if len(v) == 2:  # check if there are two numbers near an asterisk
        ans += int(v[0]) * int(v[1])  # calculate the gear ratio and add it to the answer

print(ans)
