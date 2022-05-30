import string

from words import words
from hangman import Hangman


def run():
    """ Hangman. """
    run = Hangman()

    word = run.random_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while True:
        # Display hangman visuals.
        run.display_hangman()
        # Display hangman text.
        run.display_text(word, used_letters)
        # Requesting user input.
        user_input_guess = run.user_input_guess()
        # Validating user input and conditions.
        run.validate_user_guess(
            user_input_guess, word_letters, alphabet, used_letters)

        # Out of lives condition.
        if run.dead_condition(word) == True:
            break

        # Correct word condition.
        if run.win_condition(word, word_letters) == True:
            break


if __name__ == '__main__':
    run()
