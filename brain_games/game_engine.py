import prompt


def get_rounds_in_game():
    rounds = 3
    return rounds


def engine(questions, answers, game_task):

    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    
    print(game_task)

    rounds_left = get_rounds_in_game()

    for question in questions:
        print(f'Question: {questions[rounds_left - 1]}?')
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() == str(answers[questions[rounds_left - 1]]):
            print('Correct!')
            rounds_left = rounds_left - 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was '
                f'{answers[questions[rounds_left - 1]]}. '
                f'Let\'s try again, {name}!')
            return
        
    if rounds_left == 0:
        print(f'Congratulations, {name}!')