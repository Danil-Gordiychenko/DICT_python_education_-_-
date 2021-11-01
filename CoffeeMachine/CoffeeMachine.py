print('Enter the amount of ingredients:')
water = int(input('water:'))
milk = int(input('milk:'))
beans = int(input('beans:'))
cups = int(input('cups:'))
money = int(input('money:'))
while True:
    print('Write action (buy, fill, take):')
    select = input()
    if select == 'buy':
     while True:
      print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
      drink = int(input())
      if drink == 1:
            int(input('Write how many cups of coffee you will need:'))
      if drink == 2:
            int(input('Write how many cups of coffee you will need:'))
      if drink == 3:
            int(input('Write how many cups of coffee you will need:'))
    if select == 'fill':
        while True:
         a = int(input('Write how many ml of water you want to add:'))
         add1 = a + water
         b = int(input('Write how many ml of milk you want to add:'))
         add2 = b + milk
         c = int(input('Write how many grams of coffee beans you want to add:'))
         add3 = c + beans
         v = int(input('Write how many disposable coffee cups you want to add:'))
         add4 = v + cups
         print('The coffee machine has:')
         print(add1, 'of water')
         print(add2, 'of milk')
         print(add3, 'of coffee beans')
         print(add4, 'of disposable cups')
         print(money, 'of money')
         break
    if select == 'take':
      while True:
         int(input('I gave you N'))
