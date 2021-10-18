# Этап 1
print('HANGMAN')
print('The game will be available soon.')
# Этап 2
print('Do you want to start the game?')
print('Start the game press 1; Exit press 2;')
def restart(replay):
    global start_game
number3 = input()
x=0
while x != 1:
   x = int(input())
   if x == 1:
       print('HANGMAN')
       print("Start")
   else:
       print('HANGMAN')
       print("Please, try again")
       restart('')
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
x = random.choice(my_list)

print(
    'HANGMAN')
ln = len(x) - 3
print('Guess the word:'+x[0:3]+"-"*ln)
a = input()
if a == x:
    print("You survived!")
else:
    print("You lost!")

# Этап 5
print('HANGMAN')
import random
my_list = ['python', 'java', 'javascript', 'php']
a = random.choice(my_list)
ln = len(a)
print("-"*ln)
print('Input a letter:')
y = list(a)
print(list(a))
b = input()
for c in [y]:
 if b in c:
    print("-" * ln)
    print('Input a letter:')
 else:
     print("'That letter doesn't appear in the word'")
