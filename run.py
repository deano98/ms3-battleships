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


def player_one_ships():
    """
    Get the ship coordinate input from player 1
    """
    coordinates = []
    
    for i in range(5):
        print(f"Please enter the coordinates for ship number {i + 1}")
        print("Coordinates should be A-E followed by 1-5")
        print("For example C2")

        player_one_coordinates = input("Enter your coordinates here:\n")

        coordinates.append(player_one_coordinates)

    return coordinates


def main():
    """
    Run all program functions
    """
    players = get_player_names()
    print(f"Player One: {players[0]} vs Player 2: {players[1]}")
    pprint(player_one_board)
    pprint(player_two_board)
    p1_coordinates = player_one_ships()
    print(p1_coordinates)


main()
