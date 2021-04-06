import random


def random_score(score_limit):
    return random.randrange(0, score_limit)


def new_game():
    total_score = 0
    turns = []
    first_roll_score = 0
    second_roll_score = 0

    for turn in range(10):
        first_roll_score = random_score(11)
        if first_roll_score == 10:
            turns.append(first_roll_score)
            print('Strike!!!!')
            continue
        second_roll_score = random_score(11 - first_roll_score);
        turns.append(first_roll_score + second_roll_score)
        if first_roll_score + second_roll_score == 10:
            print('Spare!!!')
    print(turns)



new_game()
