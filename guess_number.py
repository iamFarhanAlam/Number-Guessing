# no of guesses 9
# print no of guesses left
# No of guesses he took to finish
# game over
'''
------------ NUMBER GUESSESS -----------
'''

n = 74
number_guess = 1
print("No. of guesses is limited to 5 times !")
while number_guess <= 5:
    guess_number = int(input("Enter your guesses = "))
    if guess_number > 74:
        print("HIGHER !!! Enter LOWER no.\n")
    elif guess_number < 74:
        print("Lower !!! Enter HIGHER no.\n")

    else:
        print("\nMatched  wowwwww !!!!")
        break
    print(5 - number_guess, "No. of Guess Left\n")
    number_guess += 1

if number_guess > 5:
    print("GAME OVER !")