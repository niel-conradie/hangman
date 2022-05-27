import random
import string

from words import words


def random_word(words):
    """ Randomly select a word from a list. """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def play():
    """ Hangman. """
    word = random_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        # Display letters used and lives left.
        print(f"\nLives: {lives}")
        print("You have used these letters: ", ' '.join(used_letters))

        # Display current word.
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        # Requesting player input.
        player_input = input("Guess a letter: ").upper()

        # Player input validation and conditions.
        if player_input in alphabet - used_letters:
            used_letters.add(player_input)
            if player_input in word_letters:
                word_letters.remove(player_input)
            else:
                lives -= 1
                print(f"\n{player_input} is not in the word.")
        elif player_input in used_letters:
            print("\nYou have already used that character. Please try again.")
        else:
            print("\nInvalid character. Please try again.")

    # Game Won/Lost conditions.
    if lives == 0:
        print(f"\nYou have died. The word was {word}. Better luck next time!")
    else:
        print("\nCongratulations!")
        print(f"You have guessed the word {word} correctly!")


if __name__ == '__main__':
    play()
