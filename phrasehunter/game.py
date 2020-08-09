from phrasehunter.phrase import Phrase
import random
from string import ascii_letters


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = [
            Phrase("you  fail  when  you  stop  trying"),
            Phrase("what  doesnt  kill  you  makes  you  stronger"),
            Phrase("train  hard  fight  easy"),
            Phrase("float  like  a  butterfly  sting  like  a  bee"),
            Phrase("life  is  good")
        ]
        self.active_phrase = self.random_phrase()
        self.guesses = [" "]

    def start(self):
        """Call the welcome method
            starts  and run the game loop"""
        self.welcome()
        while self.missed != 5 and not self.active_phrase.check_complete(self.guesses):
            # Print missed guesses counter 
            print(f"{' '*11}Wrong guesses: {self.missed}\n")
            self.active_phrase.display(self.guesses)
            # call the get_guess method and assign it to a variable
            user_guess = self.get_guess()
            # Add the user's guess to guesses list
            self.guesses.append(user_guess)
            # Increment the number of missed attempts by 1
            if not self.active_phrase.check_letters(user_guess):
                print("Bummer!")
                self.missed += 1
        else:
            # if the guess is incorrect, calls the game_over method
            self.game_over()

    def random_phrase(self):
        """Randomly retrieve one of the phrases stored in the phrases list and return it."""
        return random.choice(self.phrases)

    def welcome(self):
        """Print a friendly welcome message to the user at the start of the game"""
        print(f"{' '*7}{' ' * 5}{'=' * 13}\n{' '*7}{' ' * 5}W_E_L_C_O_M_E\n"
              f"{' '*7}{' ' * 10}T_O\n{' '*8}P_H_R_A_S_E  H_U_N_T_E_R\n{' '*7}{'=' * 26}\n "
              f"      5 wrong guesses = looser!")

    def get_guess(self):
        """Get the guess from a user and records it in the guesses attribute"""
        while True:
            try:
                guess_input = input("\n\n Guess a letter:> ").lower()
                if len(guess_input) != 1 or not guess_input.isalpha():
                    raise ValueError("Try again using only lowercase alphabets")
            except ValueError as err:
                print(f"Invalid input {err}")
                continue
            else:
                return guess_input

    def game_over(self):
        """Displays a friendly win or loss message and ends the game.
         """
        if self.active_phrase.check_complete(self.guesses):
            print(" Congratulations\n   **You won**")
            self.replay()
        elif self.missed == 5:
            print("\n\n    Game Over!\nBetter luck next time.")
            self.replay()

    def replay(self):
        """Prompt user to play again"""
        while True:
            try:
                replay_input = input("\nWould you like to play again? Y/N:> ").lower()
                if replay_input == 'y':
                    return self.restart()
                elif replay_input == 'n':
                    print("\n*See you later*")
                    break
                elif replay_input != 'y' and replay_input != 'n':
                    raise ValueError("type a single letter: Y or N")
            except ValueError as err:
                print(f"Invalid input {err}")
                continue

    def restart(self):
        """Reset to start new game"""
        self.missed = 0
        self.guesses = [" "]
        self.active_phrase = self.random_phrase()
        self.start()

