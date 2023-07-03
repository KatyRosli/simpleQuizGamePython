from cryptography.fernet import Fernet

master_pwd = input("what is the master password? ")

'''
# this is a function that creates a key file
def write_key():
    key = Fernet.generate_key()
    # by default, the open() function opens a file in text format. 
    # As a result, the "wb" mode opens the file in binary format for writing
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''


# this is a function
def view():
    # Read Only (‘r’): Open text file for reading. 
    # The handle is positioned at the beginning of the file. 
    # If the file does not exists, raises the I/O error. 
    # This is also the default mode in which a file is opened. 
    with open('passswords.txt', 'r') as f:
        # using for loop
        for line in f.readlines():
            # rstrip means removes any trailing characters (characters at the end a string), 
            # space is the default trailing character to remove
            data = line.rstrip()
            # this means it will remove "|" 
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)

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
