# open input file
lines = open("C:\\Users\\Brendan\\AoC2023\\Day 1\\input.txt").read().splitlines()
# initialize the counter
count = 0
# for loop that reads through each line of input
for line in lines:
    digits = []
    # nested for loop that detects if there is a digit in the line
    for c in line:
        # if there is a digit, add it to the count
        if c.isdigit():
            digits.append(c)
    count += int(digits[0]+digits[-1])
print(count)
