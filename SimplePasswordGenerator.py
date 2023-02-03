import random
import string
import os
def generate_password(length):
    # Generate a random password of specified length
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

def store_password(password):
    desktopDir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    path = os.path.join(desktopDir, "passwords.txt")
    # Write the generated password to a text file
    with open(path, "a") as file:
        file.write(password + "\n")

def main():
    length = int(input("Enter the desired password length: "))
    password = generate_password(length)
    print("Generated password:", password)
    store_password(password)

if __name__ == "__main__":
    main()