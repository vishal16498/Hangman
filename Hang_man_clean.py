import random
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
word_list = ["apple", "mango", "balloon", "swim", "bike", "laptop", "book", "mobile", "mask"]
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list)
letter_to_fill = []
end_of_game = False
No_of_lives = 6
#to generate underscore list
for letter in chosen_word:
    letter_to_fill += "_"

while not end_of_game:
    user_guess = input("Guess the letter: ").lower()
    if user_guess in letter_to_fill:
        print("You have already guessed it.")
        No_of_lives -= 1
        print(f"You have {No_of_lives} lives left")
        print(stages[No_of_lives])
    for letter in range(len(chosen_word)):
        guess = chosen_word[letter]
        if guess == user_guess:
            letter_to_fill[letter] = guess
    print(" ".join(letter_to_fill))
    if user_guess not in chosen_word:
        No_of_lives -= 1
        print(stages[No_of_lives])
        print(f"You have {No_of_lives} lives left")
    if No_of_lives == 0:
        end_of_game = True
        print("You lose")
    elif "_" not in letter_to_fill:
        end_of_game = True
        print("You guessed the word correctly")



