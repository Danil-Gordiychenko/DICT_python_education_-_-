# Этап 1
print('HANGMAN')
print('The game will be available soon.')
# Этап 2
print('Do you want to start the game?')
print('Type "play" to play the game, "exit" to quit:;')
def restart(replay):
    global start_game
number3 = input()
x=0
while x != "play":
   x = input()
   if x == "play":
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
print('')
print(
    'HANGMAN')
ln = len(x) - 3
print('Guess the word:'+x[0:3]+"-"*ln)
a = input()
if a == x:
    print("You survived!")
else:
    print("You lost!")

# Этап 5-7
import random
attempts = 8
my_list = ['python', 'java', 'javascript', 'php']
a = random.choice(my_list)
y = list(a)
guessed = ['_' for n in y]
while True:
    print('')
    print('HANGMAN')
    print(''.join(guessed))
    print('Input a letter:')
    char = input()
    if char in y:
         for n, c in enumerate(y):
             if c == char:
                guessed[n] = char
         if "_" not in guessed:
             print("Thanks for playing! We'll see how well you did in the next stage")
             break
         elif char in guessed:
             print("No improvements")
             attempts -= 1
    else:
        attempts -= 1
        print("'That letter doesn't appear in the word'")
    if attempts == 0:
        print('You lost')
        break
