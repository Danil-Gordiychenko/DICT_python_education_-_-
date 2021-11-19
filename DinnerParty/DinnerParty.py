import random
y = int(input('Enter the number of friends joining (including you):\n'))
x = range(y)
buy = {}
name = 0
while True:
    if y <= 0:
        print('No one is joining for the party\n')
        break
    else:
        print('Enter the name of every friend (including you), each on a new line:')
        for i in x:
            name = str(input())
            buy[name] = 0
        number = int(input('Enter the total amount:\n'))
        li = number / y
        g = round(li, 2)
        buy = {name: g for name in buy}
        while True:
            question = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
            if question == 'Yes':
                v = random.choice(list(buy.keys()))
                print(v.title(), 'is the lucky one!')
                li = number / (y-1)
                g = round(li, 2)
                buy = {name: g for name in buy}
                buy[v] = 0
                print(buy)
                break
            else:
                print('No one is going to be lucky')
                buy = {name: g for name in buy}
                print(buy)
                break
    break
