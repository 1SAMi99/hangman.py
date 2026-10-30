import random

def pick_word(words):
    index = random.randint(0, len(words) - 1)
    word = words[index]
    return word


def display_word(guessed_word):
    print("".join(guessed_word),end = "")


def is_complete(guessed_word):
    if not "*" in guessed_word:
        return True
    else:
        return False


def reveal_letter(word, guessed_word, letter):
    found = False
    for i in range(len(word)):
        if word[i] == letter:
            guessed_word[i] = letter
            found = True
    return found


def play_one_round(words):
    word = pick_word(words)
    guessed_word = ["*"]*len(word)
    miss_counter = 0
    while True:
        print("(Guess) Enter a letter in word ", end="")
        display_word(guessed_word)
        letter = input(": ")
        letter = letter.strip().lower()
        if ("a" <= letter <= "z") == False or len(letter) > 1:
            print("Invalid input. Please enter a single English letter (a-z).")
            continue
        if letter in guessed_word:
            print(f"You have already guessed {letter}.")
        reveal = reveal_letter(word, guessed_word, letter)
        if reveal == False:
            miss_counter +=1
            print(f"{letter} is not in the word.")
        else:
            if is_complete(guessed_word):
                print(f"The word is {word}")
                print(f"Number of misses: {miss_counter}")
                break


def main():
    while True:
        words = ["program", "python", "computer", "student", "science"]
        print("Welcome to Hangman!")
        play_one_round(words)
        replay = input("Do you want to guess another word? Enter y or n: ")
        replay = replay.strip().lower()
        while replay != "y" and replay != "n":
            print("Invalid input. Please enter 'y' or 'n'.")
            replay = input("Do you want to guess another word? Enter y or n: ")
        replay = replay.strip().lower()
        if replay == "y":
            continue
        else:
            print("Goodbye!")
            break


main()