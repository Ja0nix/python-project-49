from math import gcd
from random import randint

game_task = 'Find the greatest common divisor of given numbers.'


def calc_game_data():
    answer_and_question = []

    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)

    answer_and_question.append(f'{random_num1} {random_num2}')

    answer_and_question.append(gcd(random_num1, random_num2))

    return answer_and_question