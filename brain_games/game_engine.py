import prompt


def engine(questions, answers_for_questions, game_task):

    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    
    print(game_task)

    correct_answer_count = 0
    wrong_answer_count = 0

    while(correct_answer_count < 3 and wrong_answer_count == 0):
        
        print(f'Question: {questions[correct_answer_count]}?')
        user_answer = prompt.string(f'Your answer: ')

        if user_answer.lower() == str(answers_for_questions[questions[correct_answer_count]]):
            print('Correct!')
            correct_answer_count = correct_answer_count + 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer was {answers_for_questions[questions[correct_answer_count]]}. Let\'s try again, {name}!')
            wrong_answer_count = 1

    if correct_answer_count == 3:
        print(f'Congratulations, {name}!')