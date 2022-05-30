import random

from hangman_visual import lives_visual_dict


class Hangman:
    """ A class to represent a Hangman game. """

    def __init__(self):
        """ Initialize class attributes. """
        self.lives = 6

    @staticmethod
    def random_word(words):
        """ Randomly select a word from a list. """
        word = random.choice(words)
        while '-' in word or ' ' in word:
            word = random.choice(words)
        return word.upper()

    def display_hangman(self):
        """ Display hangman visuals. """
        print(lives_visual_dict[self.lives])

    def display_text(self, word, used_letters):
        """ Display hangman information. """
        print(f"Lives: {self.lives}")
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

    @staticmethod
    def user_input_guess():
        """ Requesting user input and validating letter. """
        while True:
            try:
                user_input = input("Guess a letter: ").upper()
            except ValueError:
                print(f"\nThat is not a letter.")
                continue
            return user_input

    def validate_user_guess(self, user_input_guess, word_letters, alphabet, used_letters):
        """ User input validation and conditions. """
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
        """ Return True if out of lives. """
        if self.lives == 0:
            print(
                f"\nYou have died. The word was {word}. Better luck next time!")
            return True

    @staticmethod
    def win_condition(word, word_letters):
        """ Return True if correct word. """
        if len(word_letters) == 0:
            print("\nCongratulations!")
            print(f"You have guessed the word {word} correctly!")
            return True
