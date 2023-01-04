from sys import exit

from hangman import Hangman


def run():
    """Hangman."""
    run = Hangman()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        exit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
