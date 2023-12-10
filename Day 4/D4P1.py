# read input data and data clean by splitting |
data = open("C:\\Users\\Brendan\\AoC2023\\Day 4\\input4.txt").read().splitlines()
data = [x.split('|') for x in data]
 
# initialize winning numbers
win = [x[0][10:] for x in data]
win = [x.strip().split() for x in win]

# initialize elfs numbers
elf = [x[1] for x in data]
elf = [x.strip().split() for x in elf]

# initialize total points and final answer, along with a bool for the first win to tell if it should be multiplied
points = 0
ans = 0
firstwin = True
# iterate through input and add/multiply points from winning numbers
for i,card in enumerate(elf):
    for num in card:
        if num in win[i]:
            if firstwin:
                points += 1
                firstwin=False
            else:
                points *= 2
    # put total points into answer and reset points and firstwin bool for next game
    ans += points
    points = 0
    firstwin = True
print(ans)