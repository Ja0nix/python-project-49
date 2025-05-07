from random import randint

game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    answer_and_question = []

    random_number = randint(1, 100)
    answer_and_question.append(f'{random_number}')

    if is_prime(random_number):
        answer_and_question.append('yes')
    else:
        answer_and_question.append('no')

    return answer_and_question