from hangman import Hangman


def run():
    """Hangman."""
    run = Hangman()

    try:
        # Starting the game.
        run.start_game()
    except KeyboardInterrupt:
        # Stopping the game.
        quit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
