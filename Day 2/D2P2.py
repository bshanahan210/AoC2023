# similar solution to part 1, but now with multiplication 
# load data, data clean, and initialize the answer
data = open("C:\\Users\\Brendan\\AoC2023\\Day 2\\input2.txt").read().splitlines()
data = [x.replace(',','') for x in data]
data = [x.split(';') for x in data]
ans=0
# iterate thru each game
for d in data:
    # initialize variables to calculate the max of each color
    rmax,gmax,bmax=0,0,0
    for e in d:
        # same solution as p1 but without possible bool
        r,g,b=0,0,0
        prev=0
        ff = e.split(' ')
        for f in ff:
            match f:
                case 'red':
                    r+=int(prev)
                case 'green':
                    g+=int(prev)
                case 'blue':
                    b+=int(prev)
            prev = f
        # check if given color has more than its "max" amount, and if so make it the new max
        if r>rmax:
            rmax = r
        if g>gmax:
            gmax = g
        if b>bmax:
            bmax = b
    # multiply each max value to get its power for the final answer
    ans+=rmax*gmax*bmax
print(ans)