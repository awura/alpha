
from __future__ import division
from random import*
from statistics import*


#initializing the variable
rand = 0;
randList = []

while rand < 50:

    lister = (uniform(-5, 7))
    randList.append(str(lister))
    
    rand += 1


def randPrint():
    print(randList)
    
def randmin():
    print("Minimum: ", min(randList.append(str(lister))))

def randmax():
    print("Maximum: ", max(lister))

def randmean():
    print("Mean: ", mean(lister))

def randsort():
    print("Numbers (sorted): ", sorted(randList))

