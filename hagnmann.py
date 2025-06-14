import random
words = ["apple", "train", "chair", "house", "plant"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

guessed_letters = []

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("\nWord:", " ".join(guessed))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Enter a single letter only.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if "_" not in guessed:
    print("\nYou won! The word was:", word)
else:
    print("\nYou lost! The word was:", word)
