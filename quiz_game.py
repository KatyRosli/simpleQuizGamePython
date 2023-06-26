print("Welcome to my computer qiz!")

# note: there's a space so user can type after the question mark
playing = input("Do you want to play? ")

# if statement
if playing != "yes":
    quit()

# if true then print statement
print("Okey! Let's play :)")

answer = input("What does CPU stand for? ")
if answer == "central procession unit":
    # note: accept single qoute as well
    print('Correct!')
else:
    print('Incorrect')

answer = input("What does GPU stand for? ")
if answer == "graphics procession unit":
    print('Correct!')
else:
    print('Incorrect')

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
else:
    print('Incorrect')

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct!')
else:
    print('Incorrect')