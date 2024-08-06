import argparse
import random

class RedBlueNim:
    def __init__(self, red_pile, blue_pile, game_version, first_player='computer', depth=None):
        # """
        # Initialize the game with the given number of stones in each pile.

        # Args:
        #     red_pile (int): The number of stones in the red pile.
        #     blue_pile (int): The number of stones in the blue pile.
        #     game_version (str): The version of the game. Can be either 'standard' or 'misere'.
        #     first_player (str): The first player. Can be either 'computer' or 'human'.
        #     depth (int): Search depth for AI (optional).
        # """
        if not isinstance(red_pile, int) or not isinstance(blue_pile, int):
            raise ValueError("Both red_pile and blue_pile must be integers.")
        if red_pile < 0 or blue_pile < 0:
            raise ValueError("Both red_pile and blue_pile must be non-negative.")
        if game_version not in ['standard', 'misere']:
            raise ValueError("Invalid game version. Must be either 'standard' or 'misere'.")
        if first_player not in ['computer', 'human']:
            raise ValueError("Invalid first player. Must be either 'computer' or 'human'.")

        self.red_pile = red_pile
        self.blue_pile = blue_pile
        self.game_version = game_version
        self.first_player = first_player
        self.depth = depth

    def play_game(self):
        # """
        # Play the game until one of the piles is empty.
        # """
        initial_red_pile = self.red_pile
        initial_blue_pile = self.blue_pile

        while self.red_pile > 0 and self.blue_pile > 0:
            print(f"Welcome to the Nim_Python...! \n Initial Marbles : RED_marbles:{self.red_pile}, BLUE_marbles:{self.blue_pile}")
            # Player 1's turn
            print("Player 1's turn:")
            while True:
                move = input("Enter 'r' to remove from red pile or 'b' to remove from blue pile: ")
                if move.lower() == 'r' and self.red_pile > 0:
                    self.red_pile -= 1
                    break
                elif move.lower() == 'b' and self.blue_pile > 0:
                    self.blue_pile -= 1
                    break
                else:
                    print("Invalid move. Please try again.")

            # Player 2's turn (AI agent)
            print("Player 2's turn:")
            possible_moves = ['r', 'b']
            if self.red_pile == 0:
                possible_moves.remove('r')
            if self.blue_pile == 0:
                possible_moves.remove('b')
            move = random.choice(possible_moves)
            if move == 'r':
                self.red_pile -= 1
            elif move == 'b':
                self.blue_pile -= 1

            print(f"Red pile: {self.red_pile}, Blue pile: {self.blue_pile}")

        # Determine the winner
        if self.game_version == 'standard':
            if self.red_pile == 0 and self.blue_pile == 0:
                print("It's a tie!")
            elif self.red_pile == 0:
                print("Player 2 wins!")
            elif self.blue_pile == 0:
                print("Player 1 wins!")
        elif self.game_version == 'misere':
            if self.red_pile == 0 or self.blue_pile == 0:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")

        # Calculate the score
        if self.game_version == 'standard' and self.red_pile == 0 and self.blue_pile == 0:
            score = initial_red_pile * 2 + initial_blue_pile * 3
        else:
            score = self.red_pile * 2 + self.blue_pile * 3
        print(f"Final score: {score}")

        # Calculate the score
# if self.game_version == 'standard':
#     if self.red_pile == 0 and self.blue_pile == 0:
#         print("It's a tie! Final score: 0")
#     else:
#         score = self.red_pile * 2 + self.blue_pile * 3
#         print(f"Final score: {score}")
# elif self.game_version == 'misere':
#     if self.red_pile == 0 or self.blue_pile == 0:
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")
#     score = self.red_pile * 2 + self.blue_pile * 3
#     print(f"Final score: {score}")
 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play a game of RedBlueNim.')
    parser.add_argument('--num-red', type=int, help='Number of red marbles.', required=True)
    parser.add_argument('--num-blue', type=int, help='Number of blue marbles.', required=True)
    parser.add_argument('--version', choices=['standard', 'misere'], default='standard', help='The version of the game.')
    parser.add_argument('--first-player', choices=['computer', 'human'], default='computer', help='The first player.')
    parser.add_argument('--depth', type=int, help='Search depth for AI (optional)')

    args = parser.parse_args()
    game = RedBlueNim(args.num_red, args.num_blue, args.version, first_player=args.first_player, depth=args.depth)
    game.play_game()
