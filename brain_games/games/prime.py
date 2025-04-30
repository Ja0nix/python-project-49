from random import randint


def calc_game_data():
    answers_for_questions = {}

    questions = []
    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    prime_numbers = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        ]
    questions_in_game = 3
    i = 0

    while i < questions_in_game:
        random_number = randint(1, 100)
        questions.append(f'{random_number}')

        if random_number in prime_numbers:
            answers_for_questions[questions[i]] = 'yes'
        else:
            answers_for_questions[questions[i]] = 'no'

        i = i + 1

    return questions, answers_for_questions, game_task