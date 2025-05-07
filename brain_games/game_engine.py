import prompt


def engine(calc_game_data, game_task):

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(game_task)

    rounds = 3

    for _ in range(rounds):
        question_and_answer = calc_game_data()
        print(f'Question: {question_and_answer[0]}?')
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() == str(question_and_answer[1]):
            print('Correct!')
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was '
                f'{question_and_answer[1]}. '
                f'Let\'s try again, {name}!')
            return
        
    print(f'Congratulations, {name}!')
