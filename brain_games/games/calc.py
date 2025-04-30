from random import choice, randint


def calc_game_data():
    answers_for_questions = {}

    questions = []
    game_task = 'What is the result of the expression?'
    questions_in_game = 3
    i = 0

    operations = ['+', '-', '*']

    while i < questions_in_game:
        random_operation = choice(operations)
        random_num1 = randint(1, 10)
        random_num2 = randint(1, 10)

        questions.append(f'{random_num1} {random_operation} {random_num2}')

        if random_operation == '+':
            answers_for_questions[questions[i]] = random_num1 + random_num2

        if random_operation == '-':
            answers_for_questions[questions[i]] = random_num1 - random_num2

        if random_operation == '*':
            answers_for_questions[questions[i]] = random_num1 * random_num2

        i = i + 1

    return questions, answers_for_questions, game_task