import sys


while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('0. Exit')
    while True:
        menu_choice = int(input('Your choice:'))
        # если 1
        if menu_choice == 1:

            # Первая матрица
            size = input('Enter size of first matrix:')
            variable1 = int(size[0])
            variable = int(size[2])
            print('Enter first matrix:')
            first_list = [input().split() for x in range(variable1)]
            print(first_list)

            # Вторая матрица
            size2 = input('Enter size of second matrix:')
            variable2 = int(size2[0])
            variable3 = int(size2[2])
            print('Enter second matrix:')
            second_list = [input().split() for x in range(variable2)]
            print(second_list)
            if variable1 != variable2 and variable != variable3:
                print('ERROR')
                break

        if menu_choice == 2:
            size = input('Enter size of first matrix:')
            variable1 = int(size[0])
            variable = int(size[2])
            print('Enter first matrix:')
            first_list = [input().split() for x in range(variable1)]
            print(first_list)
            const = int(input('Enter constant:'))
            for matrix in first_list:
                print(matrix * const)

        # Если 0
        if menu_choice == 0:
            sys.exit()

