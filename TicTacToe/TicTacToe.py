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


def game_code():
    global victory
    # horizontal
    for idx in range(0, 9, 3):
        if list_new[idx] == list_new[idx + 1] == list_new[idx + 2] != '_':
            print(list_new[0], 'wins')
            victory += 1
    # vertical
    for idx in range(0, 3):
        if list_new[idx] == list_new[idx + 3] == list_new[idx + 6] != '_':
            print(list_new[0], 'wins')
            victory += 1
    # diagonal
    if list_new[0] == list_new[4] == list_new[8] != '_':
        print(list_new[0], 'wins')
        victory += 1
    elif list_new[2] == list_new[4] == list_new[6] != '_':
        print(list_new[2], 'wins')
        victory += 1
    else:
        print()


def new(isIncorrect, list_new, variable, index):
    if list_new[index] != 'X' and list_new[index] != 'O':
        list_new[index] = variable
    else:
        isIncorrect = True
        print('This cell is occupied! Choose another one!')
    return isIncorrect, list_new


if __name__ == "__main__":
    play()
    game_code()
    while True:
        try:
            z = input('Enter the coordinates:')
            s = list(z)
            xi = int(z[0])
            li = int(z[2])
            isIncorrect = False
            list_of_index = ['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3']
            if xi or li == int:
                if 0 < xi <= 3 and 0 < li <= 3:
                    for index, i in enumerate(list_of_index):
                        if z == i:
                            isIncorrect, list_new = new(isIncorrect, list_new, variable, index)
                    if not isIncorrect:
                        variable = "O" if variable == "X" else "X"
                    play()
                    game_code()
                else:
                    print('Coordinates should be from 1 to 3!')
            if victory >= 1:
                break
        except ValueError:
            print('You should enter numbers!')
