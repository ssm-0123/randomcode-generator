from json.encoder import py_encode_basestring_ascii
import random
import json

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def codes():
    a = random.choice(letters)
    b = random.choice(letters)
    c = random.choice(letters)
    d = random.choice(letters)
    return a+b+c+d

def makecode():
    fromdb = open('db.txt')
    db = fromdb.read()
    listedcoupon = json.loads(db)
    fromdb.close()
    rancode = codes()
    while True:
        if rancode in listedcoupon:
            pass
        else:
            listedcoupon.append(rancode)
            print("Your code is "+rancode)
            makedb = open('db.txt','w')
            makedb.write(json.dumps(listedcoupon))
            makedb.close()
        break

def usecode():
    fromdb = open('db.txt')
    db = fromdb.read()
    listedcoupon = json.loads(db)
    fromdb.close()
    enteredcode = input("Enter the code ")
    if enteredcode in listedcoupon:
        listedcoupon.remove(enteredcode)
        print("You used "+ enteredcode)
        makedb = open('db.txt','w')
        makedb.write(json.dumps(listedcoupon))
        makedb.close()
    else:
        print("You put the wrong code")

def reset():
    makedb = open('db.txt','w')
    makedb.write("[]")
    makedb.close()


def main():
    while True:
        print("1. Make a random code")
        print("2. Use a code")
        print("3. Reset database")
        print("4. Exit")
        pick = input("")
        if pick == "4":
            break
        elif pick == "3":
            reset()
        elif pick == "2":
            usecode()
        elif pick == "1":
            makecode()

main()
    

