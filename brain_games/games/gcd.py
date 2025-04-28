from random import randint
from math import gcd


def calc_game_data():
    answers_for_questions = {}

    questions = []
    game_task = 'Find the greatest common divisor of given numbers.'
    questions_in_game = 3
    i = 0

    while i < questions_in_game:
        random_number1 = randint(1,100)
        random_number2 = randint(1,100)

        questions.append(f'{random_number1} {random_number2}')

        answers_for_questions[questions[i]] = gcd(random_number1, random_number2)

        i = i + 1

    return questions, answers_for_questions, game_task