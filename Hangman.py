import random

print("Welcome to Hangman")
print("--------------------------------")

wordDictionary = ["hi"]

randomWord = random.choice(wordDictionary)

for x in randomWord:
    print("_", end=" ")
    
def print_Hangman(wrong):
    if (wrong == 0):
        print(" +----+")
        print(" |    |")
        print("      |")
        print("      |")
        print("      |")
        print("    ===")
    if (wrong == 1):
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("      |")
        print("      |")
        print("    ===")
    if (wrong == 2):
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print(" |    |")
        print("      |")
        print("    ===")
    if (wrong == 3):
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print(" |\   |")
        print("      |")
        print("    ===")
    if (wrong == 4):
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("      |")
        print("    ===")
    if (wrong == 5):
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("  \   |")
        print("    ===")
    if (wrong == 6):
        print(" +----+")
        print(" |    |")
        print(" o    |")
        print("/|\   |")
        print("/ \   |")
        print("    ===")

def print_word(guessedLetters):
    counter = 0
    rightLetteers = 0
    for char in randomWord:
        if (char in guessedLetters):
            print(randomWord[counter], end=" ")
            rightLetteers += 1
        else:
            print(" ", end=" ")
        counter += 1
    return rightLetteers

def print_Line():
    print("\r")
    for char in randomWord:
        print("\u203E", end=" ")

lenght_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0

while(amount_of_times_wrong != 6 and current_letters_right != lenght_of_word_to_guess):
    print("\nletters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end=" ")
    
    letterGuessed = input("\nGuesses a letter: ")
    
    if (randomWord[current_guess_index] == letterGuessed):
        print_Hangman(amount_of_times_wrong)
        
        current_guess_index +=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = print_word(current_letters_guessed)
        print_Line()
    else:
        amount_of_times_wrong +=1
        current_letters_guessed.append(letterGuessed)
        
        print_Hangman(amount_of_times_wrong)
        
        current_letters_right = print_word(current_letters_guessed)
        print_Line()
        
print("The game is over Thank you for playying :)")
        
    
