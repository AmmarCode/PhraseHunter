class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        """Print out the phrase to the console
        with guessed letters visible and un-guessed letters as underscores"""
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print("_", end=" ")

    def check_letters(self, guesses):
        """Checks to see if the letter selected by the user matches a letter in the phrase."""
        return guesses in self.phrase

    def check_complete(self, guesses):
        """Checks to see if the whole phrase has been guessed."""
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
