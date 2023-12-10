# function that creates pairs of elements from iterable
def pairs(iterable):
    iterator = iter(iterable)
    return zip(iterator, iterator)

# read input file and split it into seends and mappings
seeds, *mappings = open("C:\\Users\\Brendan\\AoC2023\\Day 5\\input5.txt").read().split('\n\n')
# extract seed values and convert them to list of ranges
seeds = seeds.split(": ")[1]
seeds = [int(value) for value in seeds.split()]
seeds = [range(start, start + length) for start, length in pairs(seeds)]
 
# process each mapping
for m in mappings:
    # skip first line and proceed to rest
    _, *ranges = m.splitlines()
    ranges = [[int(x) for x in r.split()] for r in ranges]
    ranges = [(range(a, a + c), range(b, b + c)) for a, b, c in ranges]
 
    # create new list to store updated seed ranges
    new_seeds = []

    # iterate over each seed range
    for r in seeds:
        # iterate over each mapping range
        for tr, fr in ranges:
            offset = tr.start - fr.start
            # check if seed and mapping ranges overlap
            if r.stop <= fr.start or fr.stop <= r.start:
                continue
            # calculate range between seed and mapping and left and right ranges
            ir = range(max(r.start, fr.start), min(r.stop, fr.stop))
            lr = range(r.start, ir.start)
            rr = range(ir.stop, r.stop)
            # add left and right ranges to seed list
            if lr:
                seeds.append(lr)
            if rr:
                seeds.append(rr)
            # add updated range to new seed list
            new_seeds.append(range(ir.start + offset, ir.stop + offset))
            break
        else:
            # if no overlap then add original seed ranges
            new_seeds.append(r)
    # update seeds list with new ranges
    seeds = new_seeds

# print the minimum start value from the seed ranges
print(min(x.start for x in seeds))