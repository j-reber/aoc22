import re

def move(stacks, amount, stack_from, stack_to):
    res_stack = []
    amount = int(amount)
    for s in stacks:
        if int(s[0]) == int(stack_from):
            rest = s[:-amount]
            popped = s[-amount:]
            # popped.reverse()  # Just uncomment this for the first Puzzle
    for s in stacks:
        if int(s[0]) == int(stack_to):
            res_stack.append(s + popped)
        elif int(s[0]) == int(stack_from):
            res_stack.append(rest)
        else:
            res_stack.append(s)


    return res_stack




INPUT = 'input/input1.txt'
if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().split('\n')

    start_config = []
    moves = []
    for line in lines:
        if line.startswith('move'):
            moves.append(line)
        else:
            start_config.append(line)

    parsed_moves = [re.findall(r'\d+', line) for line in moves]
    # parsed_moves = [[int(j) for j in i] for i in parsed_moves]
    parsed_config = []
    for line in start_config:
        line = re.sub('\[', ' ', line)
        line = re.sub('\]', ' ', line)
        parsed_config.append(line)

    parsed_config = [line[1:] for line in parsed_config]
    parsed_config.pop(-1)
    parsed_config.reverse()

    config = []
    for i, crate in enumerate(parsed_config[0]):
        if crate != ' ':
            tower = []
            for line in parsed_config:
                # print(i, line)
                tower.append(line[i])
                # print(tower)
            config.append(tower)

    final_config = []
    for stack in config:
        final_config.append(list(filter(' '.__ne__, stack)))

    res = final_config
    for m in parsed_moves:
        res = move(res, m[0], m[1], m[2])
        # res = move(res, 8, 1, 2)

        # print(res, '\n')

    top = ''
    for k in res:
        top += k[-1]

    print(top)



