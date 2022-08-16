from backup import getpath, AMOUNT, CORRECT_PASS, AMOUNT_TRIES, username
from getpass import getpass
import os

password = getpass(prompt="Enter your access code: ")
a = 0
while CORRECT_PASS!= password and a < AMOUNT_TRIES:
    print("warning!!!acces code invalid")
    password = getpass(prompt="Enter your access code: ")
    a += 1
    if a ==AMOUNT_TRIES:
        break
if a == 4:
    print("acces invalide")
if CORRECT_PASS == password:
    path = getpath()
    #clean
    for a in range(1, AMOUNT + 1):
        try:
            os.remove(f'{path}/Hello.{a}.txt')
        except Exception as e:
            print(e)
    #Signature
    if os.path.exists(path):
        if os.path.exists(f'{path}/rescue.txt'):
            ctn = open(f'{path}/rescue.txt', 'r')
        else:
            path = f"{path}/telegram"
            os.makedirs(path, exist_ok=True)
            ctn = ''
            if ctn == '':
                ctn= '1'
            else:
                ac = [int(el) for el in ctn.split(",")]
                last_number = ac[-1]
                ctn = f'{ctn},{last_number + 1}'

            with open(f'{path}/rescue.txt', 'a+') as file:
                file.write(ctn)
