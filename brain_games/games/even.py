from random import randint

from brain_games.game_engine import get_rounds_in_game


def even_game_data():

    answers_for_questions = {}

    questions = []
    game_task = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions_in_game = get_rounds_in_game()
    i = 0

    while i < questions_in_game:
        random_number = randint(1, 100)

        questions.append(f'{random_number}')

        if random_number % 2 == 0:
            answers_for_questions[questions[i]] = 'yes'
        else:
            answers_for_questions[questions[i]] = 'no'

        i = i + 1

    return questions, answers_for_questions, game_task