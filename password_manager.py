import random
import string


passwords ={}

#load exciting password file
try:
    with open("passwords.txt",'r')as file:
        for line in file:
            website, pwd=line.strip().split(":")
            passwords[website] =pwd
except:
    pass


def generatoe_password():
    chars=string.ascii_letters + string.digits +"!@#$%&"
    password="".join(random.choice(chars) for _ in range(8))
    return password


while True:
    print("\n---- PERSONAL PASSWORD MANAGER---")
    print("1. Save password")
    print("2. View password")
    print("3. Generate password")
    print("Exit")