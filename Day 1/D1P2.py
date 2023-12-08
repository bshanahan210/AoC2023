# open input file
lines = open("C:\\Users\\Brendan\\AoC2023\\Day 1\\input.txt").read().splitlines()
# initialize a counter
count = 0
# for loop that reads through each line of input
for line in lines:
    digits = []
    # nested for loop that detects if there is a digit and adds it to count
    for i,c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        # third for loop that detects digits that are spelled out
        for d,val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    count += int(digits[0]+digits[-1])
print(count)
