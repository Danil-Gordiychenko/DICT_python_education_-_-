# Этап 1
print('HANGMAN')
print('The game will be available soon.')
# Этап 2
print('Do you want to start the game?')
print('Type "play" to play the game, "exit" to quit:;')
while True:
    answer = input()
    if answer == "play":
        break
    elif answer == "exit":
        exit()
    else:
        print('Do you want to start the game?')
        print('Type "play" to play the game, "exit" to quit:;')
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
print('HANGMAN')
ln = len(x) - 3
print('Guess the word:'+x[0:3]+"-"*ln)
a = input()
if a == x:
    print("You survived!")
else:
    print("You lost!")
# Этап 5-8
import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w,' 'x', 'y', 'z']
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
    char = input()[0]
    lne = len(char)
    make = ''.join(map(str, guessed))
    if char in y:
         for n, c in enumerate(y):
             if c == char:
                guessed[n] = char
         if "_" not in guessed:
            print('')
            print('HANGMAN')
            print("Thanks for playing! We'll see how well you did in the next stage")
            break
    if len(make) >= 2:
        print('You should input a single letter.')
    if char not in y:
        attempts -= 1
        print("That letter doesn't appear in the word")
    if char not in alphabet:
        print('Please enter a lowercase English letter.')
    if lne >= 2:
        print('You should input a single letter.')
    if attempts == 0:
        print('You lost')
        break
