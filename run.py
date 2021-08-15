from pprint import pprint


def create_boards():
    """
    Creates the boards for each player
    """
    board = [
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' '],
    ]

    return board


def get_player_names():
    """
    Get the names from both players
    """
    player_one = input("Player 1 Name:\n")
    player_two = input("Player 2 Name:\n")

    return player_one, player_two


def player_ships(name):
    """
    Get the ship coordinate input from each player
    """
    coordinates = []
    while True:
        i = 1
        print("Coordinates should be A-E followed by 1-5")
        print("For example C2")
        while i < 6:
            player_coordinates = input(f"{name}, please enter the coordinates for ship number {i}\n")

            if player_coordinates in coordinates:
                print("You already have a ship placed here, enter another coordinate")
            elif validate_coordinates(player_coordinates):
                print("Coordinates are Valid!")
                coordinates.append(player_coordinates)
                i += 1
        break

    return coordinates


def validate_coordinates(coordinates):
    """
    Checks if the coordinates entered are valid
    Raises ValueError if they aren't valid
    """
    try:
        if len(coordinates) != 2:
            raise ValueError("Please type 2 values for your coordinates")
        elif coordinates[0] not in "ABCDEabcde":
            raise ValueError("Invalid coordinates")
        elif coordinates[1] not in "12345":
            raise ValueError("Invalid coordinates")
    except ValueError as e:
        print(f"Error: {e}, please try again.\n")
        return False

    return True


def process_coordinates(coordinates, board):
    """
    Processes the coordinates given and adds them to the board
    """    
    i = 0
    while i < 5:
        x = int(ord(coordinates[i][0].upper())) - 65
        y = int(coordinates[i][1]) - 1
        board[x][y] = "S"
        i += 1


def attack_coordinates(player_one, player_two, p1_board, p2_board):
    """
    Get the attack coordinates for each player
    """
    print("Coordinates should be A-E followed by 1-5")
    print("For example C2")
    i = 1
    
    while True:
        if i % 2 == 0:
            name = player_two
            board = p1_board
        else:
            name = player_one
            board = p2_board
        player_attack = input(f"{name}, please enter the coordinates for the opposing square to fire at:\n")
        if validate_coordinates(player_attack):       
            if process_attack_coords(player_attack, board, name):
                print("Coordinates are Valid!")
                i += 1
                check_win(board, name)


def process_attack_coords(coordinates, board, name):
    """
    Processes the coordinates given for each players attack and adds them to the board
    """
    print(board)
    print(name)
    x = int(ord(coordinates[0].upper())) - 65
    y = int(coordinates[1]) - 1
    if board[x][y] == "X":
        print("You have already attacked here, please enter another coordinate")
        return False
    elif board[x][y] == "S":
        print(f"Boom! Well done {name}, you sunk an opposing ship!")
        board[x][y] = "X"
        pprint(board)
        return True
    else:
        board[x][y] = "X"
        print(f"Bad luck {name} you missed!")
        pprint(board)
    return True


def check_win(board, name):
    """
    Checks the board to see if there are any ships remaining
    """
    i = 0
    n = 0
    while i < 5:
        if "S" in board[i]:
            n += 1
            i += 1
        else:
            i += 1
    if n > 0:
        return True
    else:
        print(f"Congratulations {name}, you have sunk all of the opposing battleships. You win!")        

        while True:
            play_again = input("Would you like to play again? y/n:\n")
            if validate_play_again(play_again):
                if play_again == "y" or play_again == "Y":
                    main()
                else:
                    print("Thanks for playing!")
                    exit()


def validate_play_again(input):
    """
    Checks if the coordinates entered are valid
    Raises ValueError if they aren't valid
    """
    try:
        if len(input) != 1:
            raise ValueError("Please type either y/n")
        elif input not in "ynYN":
            raise ValueError("Please type either y/n")
    except ValueError as e:
        print(f"Error: {e}\n")
        return False

    return True


def main():
    """
    Run all program functions
    """
    p1_board = create_boards()
    p2_board = create_boards()
    players = get_player_names()
    print(f"Player One: {players[0]} vs Player 2: {players[1]}")
    p1_coordinates = player_ships(players[0])
    p2_coordinates = player_ships(players[1])
    print(p1_coordinates)
    print(p2_coordinates)
    process_coordinates(p1_coordinates, p1_board)
    print(f"{players[0]} board:")
    pprint(p1_board)
    process_coordinates(p2_coordinates, p2_board)
    print(f"{players[1]} board:")
    pprint(p2_board)
    attack_coordinates(players[0], players[1], p1_board, p2_board)


main()
