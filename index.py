import random

class RedBlueNim:
    def __init__(self, red_pile, blue_pile, game_version):
        self.red_pile = red_pile
        self.blue_pile = blue_pile
        self.game_version = game_version

    def play_game(self):
        while self.red_pile > 0 and self.blue_pile > 0:
            print(f"Red pile: {self.red_pile}, Blue pile: {self.blue_pile}")
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
        if self.game_version == 'standard':
            if self.red_pile == 0 and self.blue_pile == 0:
                print("It's a tie! Final score: 0")
            else:
                score = self.red_pile * 2 + self.blue_pile * 3
                print(f"Final score: {score}")
        elif self.game_version == 'misere':
            if self.red_pile == 0 or self.blue_pile == 0:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            score = self.red_pile * 2 + self.blue_pile * 3
            print(f"Final score: {score}")

def main():
    red_pile = int(input("Enter the number of red marbles: "))
    blue_pile = int(input("Enter the number of blue marbles: "))
    game_version = input("Enter the game version ('standard' or 'misere'): ")
    game = RedBlueNim(red_pile, blue_pile, game_version)
    game.play_game()

if __name__ == "__main__":
    main()