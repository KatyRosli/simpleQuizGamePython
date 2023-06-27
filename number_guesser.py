import random

# # this means -5 to 10 is being generated
# r = random.randrange(-5, 11)
# print(r)

# # this means -5 to 11 is being generated
# r = random.randint(-5, 11)
# print(r)

top_of_range = input("Type a number: ")

# check if its digit -> .isdigit
if top_of_range.isdigit():
    # convert string to integer -> int
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time')
        quit()

else:
    print('Please type a number next time.')
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

# while loop
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    
    if user_guess == random_number:
        print("You got it!")
        # stop the loop once user guess it correctly
        break
    
    else:
        print("You got it wrong.")

print("You got it in", guesses, "guesses")
