list_new = list("_" * 9)
victory = 0
variable = "X"


def play():
    print("---------")
    print("| ", end="")
    for a in list_new[:3]:
        print(a, end=" ")
    print("|")
    print("| ", end="")
    for a in list_new[3:6]:
        print(a, end=" ")
    print("|")
    print("| ", end="")
    for a in list_new[6:9]:
        print(a, end=" ")
    print("|")
    print("---------")


play()


def game_code():
    global victory
    if list_new[0] == list_new[1] == list_new[2] != '_':
        print(list_new[0], 'wins')
        victory += 1
    elif list_new[3] == list_new[4] == list_new[5] != '_':
        print(list_new[3], 'wins')
        victory += 1
    elif list_new[6] == list_new[7] == list_new[8] != '_':
        print(list_new[6], 'wins')
        victory += 1
    elif list_new[0] == list_new[3] == list_new[6] != '_':
        print(list_new[0], 'wins')
        victory += 1
    elif list_new[1] == list_new[4] == list_new[7] != '_':
        print(list_new[1], 'wins')
        victory += 1
    elif list_new[2] == list_new[5] == list_new[8] != '_':
        print(list_new[2], 'wins')
        victory += 1
    elif list_new[0] == list_new[4] == list_new[8] != '_':
        print(list_new[0], 'wins')
        victory += 1
    elif list_new[2] == list_new[4] == list_new[6] != '_':
        print(list_new[2], 'wins')
        victory += 1
    else:
        print()


game_code()


while True:
    try:
        z = input('Enter the coordinates:')
        s = list(z)
        xi = int(z[0])
        li = int(z[2])
        if xi or li == int:
            if 0 < xi <= 3 and 0 < li <= 3:
                if variable == "X":
                    variable = "O"
                else:
                    variable = "X"
                if z == '1 1':
                    list_new[0] = variable
                elif z == '1 2':
                    list_new[1] = variable
                elif z == '1 3':
                    list_new[2] = variable
                elif z == '2 1':
                    list_new[3] = variable
                elif z == '2 2':
                    list_new[4] = variable
                elif z == '2 3':
                    list_new[5] = variable
                elif z == '3 1':
                    list_new[6] = variable
                elif z == '3 2':
                    list_new[7] = variable
                elif z == '3 3':
                    list_new[8] = variable
                if victory >= 1:
                    break
                play()
                game_code()
            else:
                print('Coordinates should be from 1 to 3!')
        elif xi or li != int:
            print('You should enter numbers!')
        continue
    except ValueError:
        print('You should enter numbers!')

