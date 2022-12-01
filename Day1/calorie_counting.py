INPUT = 'input/input1.txt'

if __name__ == '__main__':
    with open(INPUT) as f:
        max = 0
        curr = 0
        for line in f:
            if line == '\n':
                if curr > max:
                    max = curr
                curr = 0
            else:
                curr += int(line)

    print(max)
