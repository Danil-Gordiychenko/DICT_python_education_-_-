print('Starting to make a coffee')
print('Grinding coffee beans')
print('Boiling water')
print('Mixing boiled water with crushed coffee beans')
print('Pouring coffee into the cup')
print('Pouring some milk into the cup')
print('Coffee is ready!')
water = 200
milk = 50
mirror = 15
print('Write how many cups of coffee you will need:')
a = int(input())
water1 = a*200
milk1 = a*50
mirror1 = a*15
print("For"+str(a)+"cups of coffee you will need:")
print(water1, "ml of water")
print(milk1, "ml of milk")
print(mirror1, "g of coffee beans")
#2
print('Write how many ml of water the coffee machine has:')
b = int(input())
print('Write how many ml of milk the coffee machine has:')
c = int(input())
print('Write how many grams of coffee beans the coffee machine has:')
v = int(input())
print('Write how many cups of coffee you will need:')
a = int(input())
z = b//200
p = c//50
y = v//15
while True:
 if b // 200 < a:
  print('No, I can make only', z, 'cups of coffee')
  break
 elif c // 50 < a:
  print('No, I can make only', p,  'cups of coffee')
  break
 elif v // 15 < a:
  print('No, I can make only', y,  'cups of coffee')
  break
 elif b // 200 == a:
  print('Yes, I can make that amount of coffee')
  break
 elif c // 50 == a:
  print('Yes, I can make that amount of coffee')
  break
 elif v // 15 == a:
  print('Yes, I can make that amount of coffee')
 elif b // 200 > a:
   print('Yes, I can make that amount of coffee (and even', str(b % 200), 'more than that)')
   break
 elif c // 50 > a:
   print('Yes, I can make that amount of coffee (and even', str(c % 50), 'more than that)')
   break
 elif v // 15 > a:
   print('Yes, I can make that amount of coffee (and even', str(v % 15), 'more than that)')
   break

