import random
import sys


numbers_1 = list(range(2, 10))
numbers_2 = list(range(11, 30))
operation = ['+', '-', '*']
mark = 0


def level_1(num):
    global mark
    for i in range(num):
        random_num_1 = random.choices(numbers_1, k=2)
        random_op = random.choice(operation)
        try:
            num -= 1
            equation = f'{random_num_1[0]} {random_op} {random_num_1[1]}'
            print(random_num_1[0], random_op, random_num_1[1])
            expression = eval(equation)
            answer = int(input())
            if answer == expression:
                print('Right!')
                mark += 1
            else:
                print('Wrong!')
        except ValueError:
            print('Incorrect format.')
            num += 1
            return level_1(num)


def level_2(num):
    global mark
    for i in range(num):
        try:
            num -= 1
            random_num_2 = random.choice(numbers_2)
            equation = random_num_2 * random_num_2
            print(random_num_2)
            answer = int(input())
            if answer == equation:
                print('Right!')
                mark += 1
            else:
                print('Wrong!')
        except ValueError:
            num += 1
            print('Incorrect format.')
            return level_1(num)


while True:
    print("Which level do you want? Enter a number:")
    print("1 - simple operations with numbers 2-9")
    print("2 - integral squares of 11-29")
    level = input()
    while True:
        if level == '1':
            level_1(5)
        elif level == '2':
            level_2(5)
        else:
            print("Incorrect format.")
            break
        print("Your mark is", mark, "/ 5 Would you like to save the result? Enter yes or no.")
        final_question = input()
        if final_question == 'yes':
            name = input('What is your name?\n')
            print('The results are saved in "results.txt".')
            with open('result.txt', 'a+') as file:
                file.write(f'{name} - RESULT {mark}/5 LEVEL {level}\n')
                sys.exit(0)
        else:
            sys.exit(0)
