from random import randint

game_task = 'What number is missing in the progression?'


def calc_game_data():
    answer_and_question = []

    random_first_number = randint(1, 20)
    random_difference = randint(1, 10)
    random_length = randint(5, 10)
    random_position_to_guess = randint(1, random_length - 1)

    k = 1
    progression = f'{random_first_number}'
    number_to_guess = 0

    while k < random_length:
        if k == random_position_to_guess:
            progression = f'{progression} ..'
            number_to_guess = random_first_number + k * random_difference
        else:
            next_number = random_first_number + k * random_difference
            progression = f'{progression} {next_number}'
        k = k + 1

    answer_and_question.append(f'{progression}')

    answer_and_question.append(number_to_guess)

    return answer_and_question