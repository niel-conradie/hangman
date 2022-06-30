import string

from words import words
from hangman import Hangman


def run():
    """Hangman."""
    run = Hangman()

    # Display difficulty options.
    run.display_difficulty()
    # Requesting user input.
    user_input = run.user_input()

    while True:
        # Assign player to appropriate difficulty and select word.
        word = run.user_input_allocation(words, user_input)
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
                user_input_guess, word_letters, alphabet, used_letters
            )

            # Out of lives condition.
            if run.dead_condition(word) == True:
                # Display hangman visuals.
                run.display_hangman()
                # Reset lives.
                run.reset_player_lives()
                break

            # Correct word condition.
            if run.win_condition(word, word_letters) == True:
                # Add point to player score.
                run.add_player_score()
                # Display scoreboard.
                run.display_scoreboard()
                # Reset lives.
                run.reset_player_lives()
                break

            continue

        # Requesting user input.
        run.restart()

        continue


if __name__ == "__main__":
    run()
