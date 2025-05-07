from random import randint

game_task = 'Answer "yes" if the number is even, otherwise answer "no".'


def even_game_data():

    answer_and_question = []

    random_number = randint(1, 100)

    answer_and_question.append(f'{random_number}')

    if random_number % 2 == 0:
        answer_and_question.append('yes')
    else:
        answer_and_question.append('no')

    return answer_and_question