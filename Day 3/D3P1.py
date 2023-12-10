import re

# read input and initialize answer variable
lines = open("C:\\Users\\Brendan\\AoC2023\\Day 3\\input3.txt").read().splitlines()    
ans = 0

# iterate through each line of the input
for i, line in enumerate(lines):
    # find all matches of digits in the current line
    for m in re.finditer(r"\d+", line):
        # initialize indices of neighboring positions
        idxs = [
            (i, m.start() - 1),  # left
            (i, m.end()),        # right
        ]
        # row above the current line
        idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
        # row below the current line
        idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
        
        # count the number of special characters nearby within bounds
        count = sum(
            0 <= a < len(lines) and 0 <= b < len(lines[a]) and lines[a][b] != "."
            for a, b in idxs
        )
        
        # if there is at least one special character nearby, add the digit to the answer
        if count > 0:
            ans += int(m.group())

print(ans)
