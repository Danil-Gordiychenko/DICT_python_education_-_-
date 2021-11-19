class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee_beans += int(input("Write how many g of coffee do you want to add:\n"))
        self.cups += int(input("Write how many pieces of cup do you want to add:\n"))

    def take(self):
        global money
        print("I gave you " + str(money))
        money = 0

    def exit(self):
        exit()

    def remaining(self):
        print('The coffee machine has:')
        print(str(self.water) + ' of water')
        print(str(self.milk) + ' of milk')
        print(str(self.coffee_beans) + ' of coffee beans')
        print(str(self.cups) + ' of disposable cups')
        print(str(self.money) + ' of money')

    def espresso(self):
        n = int(input('Write how many cups of coffee you will need:'))
        if self.cups // n < 1:
            print("Sorry, not enough cups")
        elif self.water // 250 < n:
            print("Sorry, not enough water")
        elif self.coffee_beans // 16 < n:
            print("Sorry, not enough beans")
        elif self.cups // n >= 1:
            print('I have enough resources, making you a coffee!')
        elif self.water // 250 > n:
            print('I have enough resources, making you a coffee!')
        elif self.coffee_beans // 16 >= n:
            print('I have enough resources, making you a coffee!')
        self.water -= 250
        self.coffee_beans -= 16
        self.cups -= 1
        self.money += 4

    def latte(self):
        m = int(input('Write how many cups of coffee you will need:'))
        if self.cups // m < 1:
            print("Sorry, not enough cups")
        elif self.water // 350 < m:
            print("Sorry, not enough water")
        elif self.coffee_beans // 20 < m:
            print("Sorry, not enough beans")
        elif self.milk // 75 < m:
            print("Sorry, not enough milk")
        elif self.cups // m >= 1:
            print('I have enough resources, making you a coffee!')
        elif self.water // 350 > m:
            print('I have enough resources, making you a coffee!')
        elif self.coffee_beans // 16 >= m:
            print('I have enough resources, making you a coffee!')
        elif self.milk // 75 >= m:
            print('I have enough resources, making you a coffee!')
        self.water -= 350
        self.milk -= 75
        self.coffee_beans -= 20
        self.cups -= 1
        self.money += 7

    def cappuccino(self):
        m = int(input('Write how many cups of coffee you will need:'))
        if self.cups // m < 1:
            print("Sorry, not enough cups")
        elif self.water // 200 < m:
            print("Sorry, not enough water")
        elif self.coffee_beans // 12 < m:
            print("Sorry, not enough beans")
        elif self.milk // 100 < m:
            print("Sorry, not enough milk")
        elif self.cups // m >= 1:
            print('I have enough resources, making you a coffee!')
        elif self.water // 200 > m:
            print('I have enough resources, making you a coffee!')
        elif self.coffee_beans // 12 >= m:
            print('I have enough resources, making you a coffee!')
        elif self.milk // 100 >= m:
            print('I have enough resources, making you a coffee!')
            print('I have enough resources, making you a coffee!')
        self.water -= 200
        self.milk -= 100
        self.coffee_beans -= 12
        self.cups -= 1
        self.money += 6


objects = CoffeeMachine()

while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    if action == 'buy':
        while True:
            choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            if choice == '1':
                objects.espresso()
            elif choice == '2':
                objects.latte()
            elif choice == '3':
                objects.cappuccino()
            elif choice == 'back':
                break
            else:
                print("Try again")

    if action == 'fill':
        objects.fill()
    elif action == 'take':
        objects.take()
    elif action == 'remaining':
        objects.remaining()
    elif action == 'exit':
        objects.exit()
    else:
        print("Try again")
