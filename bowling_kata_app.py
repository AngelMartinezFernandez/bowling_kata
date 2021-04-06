import random


def random_score(score_limit):
    return random.randrange(0, score_limit)


def calculate_total_score(turns):
    return sum(turns, 0)


def new_game():
    turns = []
    global counter
    counter = 0

    for turn in range(10):

        first_roll_score = random_score(11)
        global bonus_score
        bonus_score = 0

        if first_roll_score == 10:
            if counter > 0:
                bonus_score += first_roll_score
                counter -= 1
            turns.append(first_roll_score+bonus_score)
            print(len(turns))
            print('Strike!!!!')
            print("Tirada 1 {} Bonus {}".format(first_roll_score, bonus_score))
            counter = 2
            continue

        if counter > 0:
            bonus_score += first_roll_score
            counter -= 1

        second_roll_score = random_score(11 - first_roll_score)

        if counter > 0:
            bonus_score += second_roll_score
            counter -= 1

        if first_roll_score + second_roll_score == 10:
            print('Spare!!!')
            turns.append(first_roll_score + second_roll_score + bonus_score)
            if counter == 0:
                counter = 1
            if len(turns) == 9:
                turns.append(2 * random_score(11))
                continue

        turns.append(first_roll_score + second_roll_score + bonus_score)
        print(len(turns))
        print("Tirada 1 {} Tirada 2 {} Bonus {}".format(first_roll_score, second_roll_score, bonus_score))

    print(turns)

    print(calculate_total_score(turns))


new_game()
