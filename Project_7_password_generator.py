#Program t generate a random password
import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

len = int(input("Enter the length of password:"))

def password_generator(len):

    password = "".join(random.choice(characters) for i in range(len))
    return password

print(password_generator(len))