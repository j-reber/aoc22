import string

INPUT = 'input/input1.txt'

def get_common_item(part1, part2):
    for char in part1:
        if char in part2:
            return char
    return ValueError


if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().split('\n')
    compartments = []
    for line in lines:
        c1 = line[:len(line)//2]
        c2 = line[len(line)//2:]
        compartments.append([c1, c2])

    score = 0
    for compartment in compartments:
        item = get_common_item(compartment[0], compartment[1])
        try:
            score += string.ascii_lowercase.index(item) + 1  # a = 0 etc
        except ValueError:
            score += string.ascii_uppercase.index(item) + 27  # A = 0 etc

    print(score)
