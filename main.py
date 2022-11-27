import random
from random import randint
import string
import hashlib
import base64
import requests
import pwnedpasswords
import os
import colorama
from colorama import Fore
import time




stuff = "ABCDEFGHIJKLMNOPQRSTUVWXYZabdefghijklmnopqrstuvwxyz0123456789<>,./#'][=-+_[#|!£$%^&*()"


passowrd = ''.join((random.choice(stuff) for i in range(12,24)))

print("[1] Password Gen")
print("[2] Decrpyt a Password")
print("[3] Check if your email or phone number has been in a data breach")
print("[4] Check if your password has been in a data breach")
print("[5] Wipe All Passwords")


options = int(input("Option >"))

if options == 1:
    web = input("What website is this password for >")
    message = passowrd
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    fullpass = web + " : " + base64_message
    print("Password:" + passowrd)
    print("Encrpyted Password: "  + base64_message)
    print("The enrypted version has been saved on in the .txt - When needed use the decrypt option")
    with open("password.txt", "a", encoding="utf-8") as file:
                    file.write(f"{fullpass}\n")
    time.sleep(5)
    os.system('python main.py')
elif options == 2:
    Passw = input("Ecnrypted Password:")
    base64_message = Passw
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print("Decrypted Password:" + message)
    time.sleep(5)
    os.system('python main.py')
elif options == 3:
    idk = input("Email or Password:")
    response = requests.get(f'https://haveibeenpwned.com/unifiedsearch/{idk}')

    if response.status_code == 403:
        print("Your Email/Phone number has  been found in a data breach")
    elif response.status_code == 200:
        print("Your Email/Phone number has not been found in a data breach")
elif options == 4:
    checkpassword = input("Passowrd:")
    done = pwnedpasswords.check(checkpassword)
    if done > 0:
        print( f"This password has been seen {done} times before")
        print("This password has been in a data breach its recommended that you changed it as soon as possible !")
    else:
        print("This password has not been seen in any data breaches and it is safe to use")
elif options == 5:
    input("Press Enter to Proceed this will delete all passwords in the .txt file !!!!!")
    file = open("password.txt","r+")
    file. truncate(0)
    file. close()

        


    

    

