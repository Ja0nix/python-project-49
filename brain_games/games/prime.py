from random import randint

from brain_games.game_engine import get_rounds_in_game


def is_prime(num):
    if num <= 3:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5 + 1), 2):
        if num % i == 0:
            return False
    return True

    
def calc_game_data():
    answers_for_questions = {}

    questions = []
    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions_in_game = get_rounds_in_game()
    i = 0

    while i < questions_in_game:
        random_number = randint(1, 100)
        questions.append(f'{random_number}')

        if is_prime(random_number):
            answers_for_questions[questions[i]] = 'yes'
        else:
            answers_for_questions[questions[i]] = 'no'

        i = i + 1

    return questions, answers_for_questions, game_task