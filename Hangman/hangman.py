# Этап 1
print('HANGMAN')
print('The game will be available soon.')
# Этап 2
print('Do you want to start the game?')
print('Start the game press 1; Exit press 2;')
number3 = input()
x=0
while x != 1:
   x = int(input())
   if x == 1:
       print('HANGMAN')
       print("Start")
   else:
       print('HANGMAN')
       print("Close")

print('')
print('HANGMAN')
print('Guess the word:')
word = input()
if word == 'python':
   print('You survived!')
else:
   print('You lost!')
# Этап 3
print('')
print('HANGMAN')
print('Guess the word:')
import random
my_list = ['python', 'java', 'javascript', 'php']
x = random.choice(my_list)
a = input()
if a == x:
    print("You survived!")
else:
    print("You lost!")
# Этап 4
import random
a = random.choice(my_list)
print('HANGMAN')
print('Guess the word',random.choice(my_list),':')
