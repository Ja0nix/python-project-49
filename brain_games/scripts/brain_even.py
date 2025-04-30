from random import randint

import prompt


def main():
    print("Welcome to the Brain Games!")

    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')

    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answer_count = 0
    wrong_answer_count = 0

    while (correct_answer_count < 3 and wrong_answer_count == 0):

        random_number = randint(1, 100)
        correct_answer = ''

        if random_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        
        print(f'Question: {random_number}?')
        user_answer = prompt.string('Your answer: ')

        if user_answer.lower() == correct_answer:
            print('Correct!')
            correct_answer_count = correct_answer_count + 1
        else:
            print(f'{user_answer} is wrong answer ;(. Correct answer '
                  f'was {correct_answer}. Let\'s try again, {name}!')
            wrong_answer_count = 1

    if correct_answer_count == 3:
        print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
