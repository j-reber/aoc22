INPUT = 'input/input1.txt'

def check_duplicate(list_to_check):
    for elem in list_to_check:
        if list_to_check.count(elem) > 1:
            return True
    return False




if __name__ == '__main__':
    with open(INPUT) as f:
        line = f.read()

    check_list = []
    for i in range(13):  # Change this number to 3 for first puzzle
        check_list.append(line[i])
    for i, char in enumerate(line):
        check_list.append(char)
        if not check_duplicate(check_list):
            print(check_list)
            res = i + 1
            break
        else:
           check_list.pop(0)

    print(res)