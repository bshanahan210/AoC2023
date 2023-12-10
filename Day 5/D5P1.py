# read input and initialize seeds and mappings variables
seeds, *mappings = open("C:\\Users\\Brendan\\AoC2023\\Day 5\\input5.txt").read().split('\n\n')

# data cleaning for seeds, extracting and converting them to a list of integers
seeds = seeds.split(": ")[1]
seeds = [int(x) for x in seeds.split()]

# iterate through each mapping
for m in mappings:
    # skip the first line and proceed to the rest
    _, *ranges = m.splitlines()

    # convert each range string to a list of integers
    ranges = [[int(x) for x in r.split()] for r in ranges]

    # create a list of tuples representing ranges
    ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]

    # define a translation function
    def translate(x):
        for a, b in ranges:
            # check if x is in the second range
            if x in b:
                # translate x using the start positions of both ranges
                return a.start + x - b.start
        # if x is not found in any range, return x as is
        return x

    # update the seeds using the translation function
    seeds = [translate(x) for x in seeds]

# print the minimum value from the updated seeds
print(min(seeds))
