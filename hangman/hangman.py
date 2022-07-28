import string

from random import choice

from words import words
from hangman_visual import lives_visual_dict


class Hangman:
    """A class to represent a Hangman game."""

    def __init__(self):
        """Initialize class attributes."""
        self.lives = 6
        self.player_score = 0

    @staticmethod
    def easy_random_word(words):
        """Randomly select a word from a list."""
        while True:
            word = choice(words)
            while "-" in word or " " in word:
                word = choice(words)

            # Length of word validation condition.
            if len(word) <= 5:
                break
            else:
                continue
        return word.upper()

    @staticmethod
    def hard_random_word(words):
        """Randomly select a word from a list."""
        while True:
            word = choice(words)
            while "-" in word or " " in word:
                word = choice(words)

            # Length of word validation condition.
            if len(word) > 5:
                break
            else:
                continue
        return word.upper()

    def user_input(self, words):
        """Requesting user input and validating choice."""
        while True:
            print("\nSelect your difficulty.")
            print("\nBeginner: Type '1'")
            print("Expert: Type '2'")

            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return self.easy_random_word(words)
            elif user_input == 2:
                return self.hard_random_word(words)

    def display_hangman(self):
        """Display hangman visuals."""
        print(lives_visual_dict[self.lives])

    def display_text(self, word, used_letters):
        """Display hangman information."""
        print(f"Lives: {self.lives}")
        print("You have used these letters: ", " ".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

    @staticmethod
    def user_input_guess():
        """Requesting user input and validating letter."""
        while True:
            try:
                user_input = input("Guess a letter: ").upper()
            except ValueError:
                print("\nThat is not a letter.")
                continue
            return user_input

    def validate_user_guess(
        self, user_input_guess, word_letters, alphabet, used_letters
    ):
        """User input validation and conditions."""
        if user_input_guess in alphabet - used_letters:
            used_letters.add(user_input_guess)
            if user_input_guess in word_letters:
                word_letters.remove(user_input_guess)
            else:
                self.lives -= 1
                print(f"\n{user_input_guess} is not in the word.")
        elif user_input_guess in used_letters:
            print("\nYou have already used that character. Please try again.")
        else:
            print("\nInvalid character. Please try again.")

    def dead_condition(self, word):
        """Return True if out of lives."""
        if self.lives == 0:
            print(f"\nYou have died. The word was {word}. Better luck next time!")
            return True

    @staticmethod
    def win_condition(word, word_letters):
        """Return True if correct word."""
        if len(word_letters) == 0:
            print("\nCongratulations!")
            print(f"You have guessed the word {word} correctly!")
            return True

    def add_player_score(self):
        """Add point to player score."""
        self.player_score += 1

    def display_scoreboard(self):
        """Display the amount of correct answers."""
        print(f"Correct: {self.player_score}")

    def reset_player_lives(self):
        """Reset lives to default value."""
        self.lives = 6

    def start_game(self):
        """Starting the hangman game."""
        # Requesting user input.
        user_input = self.user_input(words)

        while True:
            # Assign player to appropriate difficulty and select word.
            word = user_input
            word_letters = set(word)
            alphabet = set(string.ascii_uppercase)
            used_letters = set()

            while True:
                # Display visuals.
                self.display_hangman()
                self.display_text(word, used_letters)

                # Requesting user input.
                guess = self.user_input_guess()
                # Validating user input and conditions.
                self.validate_user_guess(guess, word_letters, alphabet, used_letters)

                # Out of lives condition.
                if self.dead_condition(word) == True:
                    self.display_hangman()
                    self.reset_player_lives()
                    break

                # Correct word condition.
                if self.win_condition(word, word_letters) == True:
                    self.add_player_score()
                    self.display_scoreboard()
                    self.reset_player_lives()
                    break

                continue

            # Requesting user input.
            self.restart()

            continue

    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            print("\nPlay Again?")
            print("\nYes: Type '1'")
            print("No: Type '2'")

            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return
            elif user_input == 2:
                print("\nThank you for playing!")
                quit()
