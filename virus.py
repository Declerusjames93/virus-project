from backup import getpath, AMOUNT
#computer root
path = getpath()
for a in range(1, AMOUNT + 1):
    with open(f"{path}/Hello.{a}.txt", "w") as file:
        file.write("you've been hacked")
        

