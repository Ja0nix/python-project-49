from random import randint

from brain_games.game_engine import get_rounds_in_game


def calc_game_data():
    answers_for_questions = {}

    questions = []
    game_task = 'What number is missing in the progression?'
    questions_in_game = get_rounds_in_game()
    i = 0

    while i < questions_in_game:
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

        questions.append(f'{progression}')

        answers_for_questions[questions[i]] = number_to_guess

        i = i + 1

    return questions, answers_for_questions, game_task