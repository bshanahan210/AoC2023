# same setup as part 1
data = open("C:\\Users\\Brendan\\AoC2023\\Day 4\\input4.txt").read().splitlines()
data = [x.split('|') for x in data]
 
win = [x[0][10:] for x in data]
win = [x.strip().split() for x in win]
 
elf = [x[1] for x in data]
elf = [x.strip().split() for x in elf]

# initialize array to hold scratchards
dups = []
for _ in elf:
    dups.append(1)

# iterate through input to tell wins, and put scratchcard values in array
for i,card in enumerate(elf):
    hitcount=0
    for num in card:
        if num in win[i]:
            hitcount+=1
            dups[i+hitcount]+=dups[i]
# get total
print(sum(dups))