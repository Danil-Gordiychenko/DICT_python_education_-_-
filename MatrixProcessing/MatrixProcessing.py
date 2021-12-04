import sys
import copy


while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
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

            # Проверка
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

        # Если 3
        if menu_choice == 5:
            size = input('Enter size of first matrix:').split()
            first_variable = int(size[0])
            first_variable1 = int(size[1])
            print('Enter first matrix:')
            first_list = [list(map(float, input().split())) for x in range(first_variable)]
            a = first_list

            def print_matrix(a):
                for strA in a:
                    print(strA)

            def minor(a, i, j):
                m = copy.deepcopy(a)
                del m[i]
                for i in range(len(a[0]) - 1):
                    del m[i][j]
                return m

            def det(a):
                m = len(a)
                n = len(a[0])
                if m != n:
                    return None
                if n == 1:
                    return a[0][0]
                signum = 1
                determinant = 0
                for j in range(n):
                    determinant += a[0][j] * signum * det(minor(a, 0, j))
                    signum *= -1
                return determinant
            print("\n")
            print('The result is:', det(a))

        # Если
        if menu_choice == 0:
            sys.exit(0)

