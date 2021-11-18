sim = 0
my_list = []
while True:
    num = int(input('введите количество цифр:\n'))
    while True:
        if num <= 0:
            print('Try again\n')
            break
        else:
            print('Введите числа:')
            for i in range(num):
                a = int(input())
                if a <= 0:
                    my_list.append(a)
                    sim += a
            print('Ваша сумма =', sum(my_list))
            break


