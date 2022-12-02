INPUT = 'input/input1.txt'


def calculate_score(op_score, my_score):
    """
    A, X == Rock
    B, Y == Paper
    C, Z == Scissors
    :param op_score: Sign that the opponent gave
    :param my_score: My sign
    :return: Total score that round
    """
    if op_score == 'A' and my_score == 'X':
        return 3 + 1  # Draw + Rock
    elif op_score == 'B' and my_score == 'Y':
        return 3 + 2  # Draw + Paper
    elif op_score == 'C' and my_score == 'Z':
        return 3 + 3  # Draw + Scissors
    elif op_score == 'A' and my_score == 'Y':
        return 6 + 2  # Win + Paper
    elif op_score == 'A' and my_score == 'Z':
        return 0 + 3  # Loss + Scissors
    elif op_score == 'B' and my_score == 'X':
        return 0 + 1  # Loss + Rock
    elif op_score == 'B' and my_score == 'Z':
        return 6 + 3  # Win + Scissors
    elif op_score == 'C' and my_score == 'X':
        return 6 + 1  # Win + Rock
    elif op_score == 'C' and my_score == 'Y':
        return 0 + 2  # Loss + Paper
    else:
        return 0

def calculate_sign(op_move, res):
    """
    A == Rock
    B == Paper
    C == Scissors
    X == Loss
    Y == Draw
    Z == Win
    :param op_move: Sign that the opponent is going to play
    :param res: Supposed outcome
    :return: Total score
    """
    if op_move == 'A' and res == 'X':
        return calculate_score(op_move, 'Z') # Scissors loses to Rock
    elif op_move == 'B' and res == 'Y':
        return calculate_score(op_move, 'Y') # Paper draws to Paper
    elif op_move == 'C' and res == 'Z':
        return calculate_score(op_move, 'X') # Rock wins to Scissors
    elif op_move == 'A' and res == 'Y':
        return calculate_score(op_move, 'X') # Rock draws to Rock
    elif op_move == 'A' and res == 'Z':
        return calculate_score(op_move, 'Y') # Paper wins to Rock
    elif op_move == 'B' and res == 'X':
        return calculate_score(op_move, 'X') # Rock loses to Paper
    elif op_move == 'B' and res == 'Z':
        return calculate_score(op_move, 'Z') # Scissors wins to Paper
    elif op_move == 'C' and res == 'X':
        return calculate_score(op_move, 'Y') # Paper loses to Scissors
    elif op_move == 'C' and res == 'Y':
        return calculate_score(op_move, 'Z') # Scissors draws to Scissors
    else:
        return 0





if __name__ == '__main__':
    with open(INPUT) as f:
        lines = f.read().split('\n')
    lines = [line.split(' ') for line in lines]
    score = 0
    for line in lines:
        score += calculate_sign(line[0], line[1])
    print(score)