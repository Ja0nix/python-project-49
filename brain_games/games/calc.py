from random import choice, randint

game_task = 'What is the result of the expression?'


def calc_game_data():
    answer_and_question = []

    operations = ['+', '-', '*']

    random_operation = choice(operations)
    random_num1 = randint(1, 10)
    random_num2 = randint(1, 10)

    answer_and_question.append(f'{random_num1}'
                               f' {random_operation} {random_num2}')

    if random_operation == '+':
        answer_and_question.append(random_num1 + random_num2)

    if random_operation == '-':
        answer_and_question.append(random_num1 - random_num2)

    if random_operation == '*':
        answer_and_question.append(random_num1 * random_num2)

    return answer_and_question
