master_pwd = input("what is the master password? ")

# this is a function
def view():
    # Read Only (‘r’): Open text file for reading. 
    # The handle is positioned at the beginning of the file. 
    # If the file does not exists, raises the I/O error. 
    # This is also the default mode in which a file is opened. 
    with open('passswords.txt', 'r') as f:
        # using for loop
        for line in f.readlines():
            print(line)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    # when using 'with', it opens the file and then it automatically closes the file once we are done
    # Append Only (‘a’): Open the file for writing. 
    # The file is created if it does not exist. 
    # The handle is positioned at the end of the file. 
    # The data being written will be inserted at the end, after the existing data.
    with open('passswords.txt', 'a') as f:
        # file name is f
        f.write(name + "|" + pwd + "\n")


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        # calling the view function
        view()
    elif mode == "add":
        # calling the add function
        add()
    else:
        print("Invalid mode.")
        continue
