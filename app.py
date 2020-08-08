# Import your Game class
from phrasehunter.game import Game

# Create Dunder Main statement.
if __name__ == '__main__':
    # Inside Dunder Main:
    # Create an instance of Game class
    # Start game by calling the instance method that starts the game loop
    game = Game()
    game.start()