water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def ingredients():
    print('The coffee machine has:')
    print(str(water) + ' of water')
    print(str(milk) + ' of milk')
    print(str(coffee_beans) + ' of coffee beans')
    print(str(cups) + ' of disposable cups')
    print(str(money) + ' of money')


def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
    global water, milk, coffee_beans, money, cups
    drink = input()
    if drink == '1':
        n = int(input('Write how many cups of coffee you will need:'))
        if cups // n < 1:
            print("Sorry, not enough cups")
        elif water // 250 < n:
            print("Sorry, not enough water")
        elif coffee_beans // 16 < n:
            print("Sorry, not enough beans")
        elif cups // n >= 1:
            print('I have enough resources, making you a coffee!')
        elif water // 250 > n:
            print('I have enough resources, making you a coffee!')
        elif coffee_beans // 16 >= n:
            print('I have enough resources, making you a coffee!')
        water -= 250
        coffee_beans -= 16
        cups -= 1
        money += 4
        return 'espresso'
    elif drink == '2':
        m = int(input('Write how many cups of coffee you will need:'))
        if cups // m < 1:
            print("Sorry, not enough cups")
        elif water // 350 < m:
            print("Sorry, not enough water")
        elif coffee_beans // 20 < m:
            print("Sorry, not enough beans")
        elif milk // 75 < m:
            print("Sorry, not enough milk")
        elif cups // m >= 1:
            print('I have enough resources, making you a coffee!')
        elif water // 350 > m:
            print('I have enough resources, making you a coffee!')
        elif coffee_beans // 16 >= m:
            print('I have enough resources, making you a coffee!')
        elif milk // 75 >= m:
            print('I have enough resources, making you a coffee!')
        water -= 350
        milk -= 75
        coffee_beans -= 20
        cups -= 1
        money += 7
        return 'latte'
    elif drink == '3':
        m = int(input('Write how many cups of coffee you will need:'))
        if cups // m < 1:
            print("Sorry, not enough cups")
        elif water // 200 < m:
            print("Sorry, not enough water")
        elif coffee_beans // 12 < m:
            print("Sorry, not enough beans")
        elif milk // 100 < m:
            print("Sorry, not enough milk")
        elif cups // m >= 1:
            print('I have enough resources, making you a coffee!')
        elif water // 200 > m:
            print('I have enough resources, making you a coffee!')
        elif coffee_beans // 12 >= m:
            print('I have enough resources, making you a coffee!')
        elif milk // 100 >= m:
            print('I have enough resources, making you a coffee!')
            print('I have enough resources, making you a coffee!')
        water -= 200
        milk -= 100
        coffee_beans -= 12
        cups -= 1
        money += 6
        return 'cappuccino'
    elif drink == 'back':
        return 'back'


def fill():
    global water, milk, coffee_beans, money, cups
    print("Write how many ml of water you want to add:")
    add_water = int(input())
    water += add_water
    print("Write how many ml of milk you want to add:")
    add_milk = int(input())
    milk += add_milk
    print("Write how many grams of coffee beans you want to add:")
    add_coffee_beans = int(input())
    coffee_beans += add_coffee_beans
    print("Write how many disposable coffee cups you want to add:")
    add_cups = int(input())
    cups += add_cups


def activity():
    print('\nWrite action (buy, fill, take, remaining, exit):')
    y = str(input())
    if y == 'buy':
        print('')
        buy()
        return 'buy'
    elif y == 'fill':
        print('')
        fill()
        return 'fill'
    elif y == 'take':
        take()
        return 'take'
    elif y == 'remaining':
        print('')
        ingredients()
        return 'remaining'
    elif y == 'exit':
        return 'exit'


class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def remaining(self):
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.coffee_beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:')
        global water, milk, coffee_beans, money, cups
        answer_user = input()
        if answer_user == str(1):
            buy()
            self.water -= 250
            self.coffee_beans -= 16
            self.cups -= 1
            self.money += 4
        elif answer_user == str(2):
            buy()
            self.water -= 350
            self.milk -= 75
            self.coffee_beans -= 20
            self.cups -= 1
            self.money += 7
        elif answer_user == str(3):
            buy()
            self.water -= 200
            self.milk -= 100
            self.coffee_beans -= 12
            self.cups -= 1
            self.money += 6
        elif answer_user == 'back':
            return 'back'

    def fill(self):
        global water, milk, coffee_beans, money, cups
        print("Write how many ml of water you want to add:")
        add_water = int(input())
        self.water += add_water
        print("Write how many ml of milk you want to add:")
        add_milk = int(input())
        self.milk += add_milk
        print("Write how many grams of coffee beans you want to add:")
        add_coffee_beans = int(input())
        self.coffee_beans += add_coffee_beans
        print("Write how many disposable coffee cups you want to add:")
        add_cups = int(input())
        self.cups += add_cups

    def take(self):
        global money
        print("I gave you " + str(money))
        money = 0

    def activity(self):
        print('\nWrite action (buy, fill, take, remaining, exit):')
        y = str(input())
        if y == 'buy':
            print('')
            objects.buy()
            return 'buy'
        elif y == 'fill':
            print('')
            objects.fill()
            return 'fill'
        elif y == 'take':
            objects.take()
            return 'take'
        elif y == 'remaining':
            print('')
            objects.remaining()
            return 'remaining'
        elif y == 'exit':
            return 'exit'


objects = CoffeeMachine()

while_action = 0

while while_action != 'exit':
    while_action = activity()

