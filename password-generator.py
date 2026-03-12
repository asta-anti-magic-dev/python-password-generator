import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))
number = int(input("How many passwords do you want? "))

characters = string.ascii_letters + string.digits + string.punctuation

print("\nGenerated Passwords:\n")

for i in range(number):
    password = ""

    for j in range(length):
        password += random.choice(characters)

    print(password)