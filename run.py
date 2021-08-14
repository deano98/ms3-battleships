from pprint import pprint

player_one_board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]

player_two_board = [
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' '],
]


def get_player_names():
    """
    Get the names from both players
    """
    player_one = input("Player 1 Name:\n")
    player_two = input("Player 2 Name:\n")

    return player_one, player_two


def player_ships(name):
    """
    Get the ship coordinate input from player 1
    """
    coordinates = []
    while True:
        i = 1

        print("Coordinates should be A-E followed by 1-5")
        print("For example C2")
        while i < 6:
            player_one_coordinates = input(f"{name} Please enter the coordinates for ship number {i}\n")

            if validate_coordinates(player_one_coordinates):
                print("Coordinates are Valid!")
                coordinates.append(player_one_coordinates)
                i += 1
        break

    return coordinates


def validate_coordinates(values):
    """
    Checks if the coordinates entered are valid
    Raises ValueError if they aren't valid
    """
    try:
        if len(values) != 2:
            raise ValueError("Please type 2 values for your coordinates")
        elif values[0] not in "ABCDEabcde":
            raise ValueError("Invalid coordinates")
        elif values[1] not in "12345":
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


def main():
    """
    Run all program functions
    """
    players = get_player_names()
    print(f"Player One: {players[0]} vs Player 2: {players[1]}")
    p1_coordinates = player_ships(players[0])
    p2_coordinates = player_ships(players[1])
    print(p1_coordinates)
    print(p2_coordinates)
    process_coordinates(p1_coordinates, player_one_board)
    print(f"{players[0]} board:")
    pprint(player_one_board)
    process_coordinates(p2_coordinates, player_two_board)
    print(f"{players[1]} board:")
    pprint(player_two_board)


main()
