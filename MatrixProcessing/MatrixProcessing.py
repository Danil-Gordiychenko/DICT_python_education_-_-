import sys
import copy


def matrix_input():
    size = input().split()
    first_variable = int(size[0])
    print('Enter first matrix:')
    first_list = [list(map(float, input().split())) for x in range(first_variable)]
    return first_list


def choice_1():
    print('Enter size of first matrix:')
    first_list = matrix_input()
    print('Enter size of second matrix:')
    second_list = matrix_input()
    if len(first_list) == len(second_list) and len(first_list[0]) == len(second_list[0]):
        print("The result is: ")
        result = [[first_list[i][j] + second_list[i][j] for j in range
        (len(first_list[0]))] for i in range(len(first_list))]
        for r in result:
            print(r)
    else:
        print("ERROR")


def choice_2():
    print('Enter size of matrix:')
    first_list = matrix_input()
    const = float(input('Enter constant:\n'))
    for i in first_list:
        for j in i:
            j *= const
            print(j, end=' ')
        print()


def choice_3():
    print('Enter size of first matrix:')
    first_list = matrix_input()
    print('Enter size of second matrix:')
    second_list = matrix_input()
    if len(first_list) == len(second_list[0]):
        answer = 0
        print("The result is: ")
        for i in range(len(first_list)):
            for j in range(len(second_list[0])):
                for k in range(len(second_list)):
                    answer += (first_list[i][k]) * (second_list[k][j])
                print(answer, end=" ")
                answer = 0
            print("")
    else:
        print('The operation cannot be performed.')


def trans():
    print('Enter size of matrix:')
    first_list = matrix_input()
    for j in range(len(first_list)):
        for i in range(len(first_list[0])):
            print(first_list[i][j], end=' ')
        print('')


def trans_2():
    print('Enter size of matrix:')
    first_list = matrix_input()
    qwe = [[first_list[j][i] for j in range(len(first_list))] for i in range(len(first_list[0]))]
    print("The result is: ")
    for z in range(len(first_list)):
        for w in reversed(qwe[z]):
            print(w, end=' ')
        print('')


def trans_3():
    print('Enter size of matrix:')
    first_list = matrix_input()
    print("The result is: ")
    for z in range(len(first_list)):
        for w in reversed(first_list[z]):
            print(w, end=' ')
        print('')


def trans_4():
    print('Enter size of matrix:')
    first_list = matrix_input()
    m = [y for y in reversed(first_list)]
    print("The result is: ")
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end=' ')
        print('')


def choice_5():
    print('Enter size of matrix:')
    a = matrix_input()

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

    print('The result is:', det(a))


while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    print('0. Exit')
    while True:
        menu_choice = input('Your choice:')
        if menu_choice == '1':
            choice_1()
        elif menu_choice == '2':
            choice_2()
        elif menu_choice == '3':
            choice_3()
        elif menu_choice == '4':
            print('1. Main diagonal')
            print('2. Side diagonal')
            print('3. Vertical line')
            print('4. Horizontal line')
            menu_choice_2 = int(input())
            if menu_choice_2 == '1':
                trans()
            elif menu_choice_2 == '2':
                trans_2()
            elif menu_choice_2 == '3':
                trans_3()
            elif menu_choice_2 == '4':
                trans_4()
        elif menu_choice == '5':
            choice_5()
        elif menu_choice == '6':
            continue
        elif menu_choice == '0':
            sys.exit(0)
        else:
            print('Try again')
            break
