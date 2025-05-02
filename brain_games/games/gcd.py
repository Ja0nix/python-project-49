from math import gcd
from random import randint

from brain_games.game_engine import get_rounds_in_game


def calc_game_data():
    answers_for_questions = {}

    questions = []
    game_task = 'Find the greatest common divisor of given numbers.'
    questions_in_game = get_rounds_in_game()
    i = 0

    while i < questions_in_game:
        random_num1 = randint(1, 100)
        random_num2 = randint(1, 100)

        questions.append(f'{random_num1} {random_num2}')

        answers_for_questions[questions[i]] = gcd(random_num1, random_num2)

        i = i + 1

    return questions, answers_for_questions, game_task