# open the input data 
data = open("C:\\Users\\Brendan\\AoC2023\\Day 2\\input2.txt").read().splitlines()
# data cleaning, replace commas with space and split the rounds of games based on semicolons
data = [x.replace(',','') for x in data]
data = [x.split(';') for x in data]
# initialize variables for the final answer and for round number
ans=0
round=1
# nested for loops that iterate through each round and count number of red, blue, and green cubes
for d in data:
    for e in d:
        # initialize red green and blue variables respectively, along with prev and possibility bool
        r,g,b=0,0,0
        prev=0
        possible=True
        ff = e.split(' ')
        for f in ff:
            match f:
                # add total amount of each game to initialized red green and blue variables
                case 'red':
                    r+=int(prev)
                case 'green':
                    g+=int(prev)
                case 'blue':
                    b+=int(prev)
            prev = f
        # we know it is not possible if there are more than 12 red, 13 green, or 14 blue
        if r>12 or g>13 or b>14:
            possible=False
            break
    # if it is possible, add it to final answer and go to next round
    if possible == True:
        ans+=round
    round+=1
print(ans)