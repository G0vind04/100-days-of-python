import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

guess = input("Guess a letter: ").lower()
placeholder=""
word_length=len(chosen_word)
for i in range(0,word_length):
    placeholder+="_"
print(placeholder)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display=""
for letter in chosen_word:
    if letter == guess:
        display+=letter
    else:
        display+="_"
print(display)
