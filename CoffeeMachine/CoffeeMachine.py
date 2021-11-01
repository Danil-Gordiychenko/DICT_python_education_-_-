print('CoffeeMachine')
water = 550
milk = 540
beans = 120
cups = 9
money = 550
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    select = input()
    if select == 'buy':
     while True:
         print('The coffee machine has:')
         print(water, 'of water')
         print(milk, 'of milk')
         print(beans, 'of coffee beans')
         print(cups, 'of disposable cups')
         print(money, 'of money')
         print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
         drink = int(input())
         if drink == 1:
          n = int(input('Write how many cups of coffee you will need:'))
          water = water - 250 * n
          beans = beans - 16 * n
          money = money + 4 * n
          print('The coffee machine has:')
          print(water, 'of water')
          print(milk, 'of milk')
          print(beans, 'of coffee beans')
          print(cups, 'of disposable cups')
          print(money, 'of money')
          break
         if drink == 2:
             n = int(input('Write how many cups of coffee you will need:'))
             water = water - 350 * n
             milk = milk - 75 * n
             beans = beans - 20 * n
             money = money + 6 * n
             print('The coffee machine has:')
             print(water, 'of water')
             print(milk, 'of milk')
             print(beans, 'of coffee beans')
             print(cups, 'of disposable cups')
             print(money, 'of money')
             break
         if drink == 3:
          z = int(input('Write how many cups of coffee you will need:'))
         water = water - 200 * z
         milk = milk - 100 * z
         beans = beans - 12 * z
         money = money + 6 * z
         print('The coffee machine has:')
         print(water, 'of water')
         print(milk, 'of milk')
         print(beans, 'of coffee beans')
         print(cups, 'of disposable cups')
         print(money, 'of money')
         break
    if select == 'fill':
        while True:
         a = int(input('Write how many ml of water you want to add:'))
         water = a + water
         b = int(input('Write how many ml of milk you want to add:'))
         milk = b + milk
         c = int(input('Write how many grams of coffee beans you want to add:'))
         beans = c + beans
         v = int(input('Write how many disposable coffee cups you want to add:'))
         cups = v + cups
         print('The coffee machine has:')
         print(water, 'of water')
         print(milk, 'of milk')
         print(beans, 'of coffee beans')
         print(cups, 'of disposable cups')
         print(money, 'of money')
         break
    if select == 'take':
      while True:
         print('I gave you', money)
         money = money * 0
         break
    if select == 'exit':
        exit()
    if select == 'remaining':
        print('The coffee machine has:')
        print(water, 'of water')
        print(milk, 'of milk')
        print(beans, 'of coffee beans')
        print(cups, 'of disposable cups')
        print(money, 'of money')
        break
