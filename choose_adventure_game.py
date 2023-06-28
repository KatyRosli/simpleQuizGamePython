name = input("type your name: ")
print("Welcome", name, "to this adventure game!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":

elif answer == "right":

else:
    print('Not a valid option. You lose.')