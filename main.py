import random
player_positions = {1: 0, 2: 0, 3: 0, 4: 0}
def roll_dice():
    return random.randint(1, 6)
def check_winner(player, position):
    if position >= 100: 
        print(f"Player {player} has won the game!")
        return True
    return False
def ludo_game():
    print("Welcome to Ludo!")
    num_players = int(input("Enter the number of players (2-4): "))
    players = list(range(1, num_players + 1))
    print("\nStarting positions: ", player_positions)
    game_over = False
    while not game_over:
        for player in players:
            input(f"\nPlayer {player}, press Enter to roll the dice...")
            dice_roll = roll_dice()
            print(f"Player {player} rolled a {dice_roll}!")
            player_positions[player] += dice_roll
            if check_winner(player, player_positions[player]):
                game_over = True
                break
            print(f"Player {player} is now at position {player_positions[player]}")
if __name__ == "__main__":
    ludo_game()