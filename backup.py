# from os import platform
import os 
import platform
username = os.getlogin()
def getpath():
    if platform.system() =="Windows":
        root = f"C:/Users/{username}"
    else:
        root = f"/home/{username}"
    return root
AMOUNT = 2
CORRECT_PASS = "1993"
AMOUNT_TRIES = 4
