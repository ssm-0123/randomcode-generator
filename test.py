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
    fromdb = open('db2.txt')
    db = fromdb.read()
    listedcoupon = json.loads(db)
    fromdb.close()
    rancode = codes()
    while True:
        if rancode in listedcoupon:
            print(rancode+" is already exist")
            pass
        else:
            listedcoupon.append(rancode)
            print("Your code is "+rancode)
            makedb = open('db2.txt','w')
            makedb.write(json.dumps(listedcoupon))
            makedb.close()
        break

def make100code():
    while True:
        fromdb = open('db2.txt')
        db = fromdb.read()
        listedcoupon = json.loads(db)
        fromdb.close()
        rancode = codes()
        if len(listedcoupon)==100:
            break
        while True:
            if rancode in listedcoupon:
                pass
            else:
                listedcoupon.append(rancode)
                makedb = open('db2.txt','w')
                makedb.write(json.dumps(listedcoupon))
                makedb.close()
            break
        
def hackcode():
    attempt = 0
    while True:
        fromdb = open('db2.txt')
        db = fromdb.read()
        listedcoupon = json.loads(db)
        fromdb.close()
        enteredcode = codes()
        if enteredcode in listedcoupon:
            listedcoupon.remove(enteredcode)
            print("You used "+ enteredcode)
            makedb = open('db2.txt','w')
            makedb.write(json.dumps(listedcoupon))
            makedb.close()
            print(attempt)
            break
        else:
            attempt = attempt + 1

def howmanycode():
    fromdb = open('db2.txt')
    db = fromdb.read()
    listedcoupon = json.loads(db)
    print(len(listedcoupon))

def reset():
    makedb = open('db2.txt','w')
    makedb.write("[]")
    makedb.close()


reset()
