import re

INPUT = 'input/input1.txt'

def count_complete_overlap(begin1, end1, begin2, end2):
    if begin1 <= begin2 and end1 >= end2:  # First responsibilities are contained in second
        # print(group)
        return 1
    elif begin1 >= begin2 and end1 <= end2:  # Second responsibilities are contained in first
        return 1
    else:
        return 0

def count_partial_overlap(begin1, end1, begin2, end2):
    if end1 >= begin2 and begin1 <= end2:  # First responsibilities are contained in second
        print(group)
        return 1
    else:
        return 0


if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().split('\n')
    responsibilities = []
    for line in lines:
        res = re.split(',|-', line)
        res = [int(i) for i in res]
        responsibilities.append(res)


    count_complete = 0
    count_partial = 0
    for group in responsibilities:
        count_complete += count_complete_overlap(group[0], group[1], group[2], group[3])
        count_partial += count_partial_overlap(group[0], group[1], group[2], group[3])

    print(count_partial)