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
                if list_new[0] != 'X' and list_new[0] != 'O':
                    list_new[0] = variable
                else:
                    print('This cell is occupied! Choose another one!')
                    if variable == "X":
                        variable = "O"
                    else:
                        variable = "X"
            elif z == '1 2':
                if list_new[1] != 'X' and list_new[1] != 'O':
                    list_new[1] = variable
                else:
                    print('This cell is occupied! Choose another one!')
            elif z == '1 3':
                if list_new[2] != 'X' and list_new[2] != 'O':
                    list_new[2] = variable
                else:
                    print('This cell is occupied! Choose another one!')
            elif z == '2 1':
                if list_new[3] != 'X' and list_new[3] != 'O':
                    list_new[3] = variable
                else:
                    print('This cell is occupied! Choose another one!')
            elif z == '2 2':
                if list_new[4] != 'X' and list_new[4] != 'O':
                    list_new[4] = variable
                else:
                    print('This cell is occupied! Choose another one!')
            elif z == '2 3':
                if list_new[5] != 'X' and list_new[5] != 'O':
                    list_new[5] = variable
                else:
                    print('This cell is occupied! Choose another one!')
            elif z == '3 1':
                if list_new[6] != 'X' and list_new[6] != 'O':
                    list_new[6] = variable
                else:
                    print('This cell is occupied! Choose another one!')
            elif z == '3 2':
                if list_new[7] != 'X' and list_new[7] != 'O':
                    list_new[7] = variable
                else:
                    print('This cell is occupied! Choose another one!')
            elif z == '3 3':
                if list_new[8] != 'X' and list_new[8] != 'O':
                    list_new[8] = variable
                else:
                    print('This cell is occupied! Choose another one!')
        else:
            print('Coordinates should be from 1 to 3!')
    elif xi or li != int:
        print('You should enter numbers!')
    if victory >= 1:
        break
    play()
    game_code()


