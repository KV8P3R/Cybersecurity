import random
import string

characters = string.ascii_letters + string.digits + "!@#$"

password = ""

for i in range(12):
    password += random.choice(characters)

print(password)
