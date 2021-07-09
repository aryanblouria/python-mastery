import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

stages = hangman_art.stages
logo = hangman_art.logo
print(logo)

#Testing code
#print(f'The solution is "{chosen_word}".')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"\nThe word is: {' '.join(display)}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
      print("You have already guessed " + guess)

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word, {lives-1} lives remaining.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was '{chosen_word}'")

    #Join all the elements in the list and turn it into a string.
    if lives > 0:
      print(f"\n{' '.join(display)}")
  
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])