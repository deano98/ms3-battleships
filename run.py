def get_player_names():
    """
    Get the names from both players
    """
    player_one = input("Player 1 Name:\n")
    player_two = input("Player 2 Name:\n")

    return player_one, player_two


players = get_player_names()
print(f"Player One: {players[0]} vs Player 2: {players[1]}")
