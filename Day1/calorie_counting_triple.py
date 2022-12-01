import re

INPUT = 'input/input1.txt'

if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().split('\n')

    sublist = []
    sublists = []
    for line in lines:
        if line == '':
            sublists.append(sublist)
            sublist = []
        else:
            sublist.append(int(line))

    added_lists = [sum(l) for l in sublists]
    tot_max = 0
    for i in range(3):
        tot_max += max(added_lists)
        added_lists.remove(max(added_lists))

    print(tot_max)

