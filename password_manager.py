from cryptography.fernet import Fernet

'''
# this is a function that creates a key file
def write_key():
    key = Fernet.generate_key()
    # by default, the open() function opens a file in text format. 
    # As a result, the "wb" mode opens the file in binary format for writing
    with open("key.key", "wb") as key_file:
        key_file.write(key) '''

# this is a function that loads the key file
def load_key():
    # "rb" option opens the file in binary format for reading
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# encode() method encodes the string, using the specified encoding
key = load_key()
fer = Fernet(key)

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
            if "|" not in data:
                continue
            # this means it will remove "|" 
            user, passw = data.split("|")
            print("User:", user, "| Password:", 
                  fer.decrypt(passw.encode()).decode())

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
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


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
