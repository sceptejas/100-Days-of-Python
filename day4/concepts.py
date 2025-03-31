# khan academy: pseudo random number gen video
from my_module import myFavNum #we made this module 
import random
# randi = random.randint(1,10) # includes 10 
# print(randi)
# print(myFavNum)

def rdotr():
    randomNumber0to1 = random.random() * 10 #this make is start from zero and go up to whatever 
    print(randomNumber0to1)

def randUni():
    randomFloat = random.uniform(1,10)
    print(randomFloat)

def toss():
    tossResult = random.randint(1,2)
    if tossResult == 1:
        print("heads")
        print(tossResult)
    else:
        print("tails")
        print(tossResult)
toss()