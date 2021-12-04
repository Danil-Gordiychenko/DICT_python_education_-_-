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
            size = input('Enter size of first matrix:').split()
            first_variable = int(size[0])
            first_variable1 = int(size[1])
            print('Enter first matrix:')
            first_list = [list(map(float, input().split()))for x in range(first_variable)]

            # Вторая матрица
            size = input('Enter size of second matrix:').split()
            second_variable = int(size[0])
            second_variable1 = int(size[1])
            print('Enter second matrix:')
            second_list = [list(map(float, input().split()))for x in range(second_variable)]
            if first_variable1 != second_variable1 and first_variable != second_variable:
                print('ERROR')
                break
            else:
                result = [[first_list[i][j] + second_list[i][j] for j in range
                (len(first_list[0]))] for i in range(len(first_list))]
                for r in result:
                    print(r)

        # если 2
        if menu_choice == 2:
            size = input('Enter size of matrix:').split()
            variable = int(size[0])
            print('Enter matrix:')
            first_list = [list(map(float, input().split()))for x in range(variable)]
            const = float(input('Enter constant:\n'))
            for i in first_list:
                for j in i:
                    j *= const
                    print(j, end=' ')
                print()
        if menu_choice == 3:
            continue

        # Если 0
        if menu_choice == 0:
            sys.exit(0)

