import string

INPUT = 'input/input1.txt'

def get_common_item_3(part1, part2, part3):
    for char in part1:
        if char in part2 and char in part3:
            return char
    return ValueError

if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().split('\n')
    compartments = []
    it = enumerate(lines)

    items_per_group = []
    for i, line in it:
        _, rucksack_2 = next(it)
        _, rucksack_3 = next(it)
        items_per_group.append(get_common_item_3(line, rucksack_2, rucksack_3))

    score = 0
    for item in items_per_group:
        try:
            score += string.ascii_lowercase.index(item) + 1  # a = 0 etc
        except ValueError:
            score += string.ascii_uppercase.index(item) + 27  # A = 0 etc

    print(score)

