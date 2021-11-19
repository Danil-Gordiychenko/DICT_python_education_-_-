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
        for i in x:
            buy = {name: li for name in buy}
        print(buy)
        break
