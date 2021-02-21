'''
Created on Feb 20, 2021
This program is to simulate how many times it takes to draw 5 different colored sticks from a lot of 1000 and finding the average number of times 
pulled to reach all 5 at least once.
@author: Tony
'''

import random
from pip._vendor.msgpack.fallback import xrange


globalkeylist = []
bluestatus = False
greenstatus = False
redstatus = False
purplestatus = False
yellowstatus = False
counter = 0
population = 1000
def setup():
    ''' keylist is the position number of the colored stick in the pot. To save processing power, the position of the stick will be static
       for the trial as it will be assigned to globalkeylist, but can be reset every time a stick is drawn to simulate further randomness if desired in future tests
    '''
    #keylist = []
    global population
    population = int(input("how many sticks are in the pot?"))
    while population < 5:
        population = int(input("please enter a number greater than or equal to 5"))
     
    global globalkeylist
    keylist = random.sample(range(0,population),5)
    globalkeylist=keylist
    
    ''' The below is a highly inefficient way to preserve the uniqueness of each color in the lot. The problem is that randomn gen can sometimes assign 
    the same value to different colors, messing up the trial. Edit (8:31PM 2/20) replaced below block with upper block code.
    '''   
    
    '''
    blue = random.randint(0,population)
    keylist.append(blue)
    red = random.randint(0,population)
    while red == blue:
        red = random.randint(0,population)
    keylist.append(red)
    green = random.randint(0,population)
    while green == red or green == blue:
        green = random.randint(0,population)
    keylist.append(green)
    yellow = random.randint(0,population)
    while yellow == red or yellow == blue or yellow == green:
        yellow = random.randint(0,population)
    keylist.append(yellow)
    purple = random.randint(0,population)
    while purple == red or purple == yellow or purple == blue or purple == green:
        purple = random.randint(0,population)
    keylist.append(purple)
    global globalkeylist
    globalkeylist=keylist
    '''
    
def drawnlots():
    global globalkeylist
    global population
    draw = random.randint(0,population)
    blue,red,green,yellow,purple = globalkeylist
    if draw == blue:
        global bluestatus
        bluestatus = True
    elif draw == green:
        global greenstatus
        greenstatus = True
    elif draw == yellow:
        global yellowstatus
        yellowstatus = True
    elif draw == red:
        global redstatus
        redstatus = True
    elif draw == purple:
        global purplestatus
        purplestatus = True

def globalreset():
    global globalkeylist
    global bluestatus
    global redstatus
    global greenstatus
    global yellowstatus
    global purplestatus
    globalkeylist = []
    bluestatus = False
    redstatus = False
    greenstatus = False
    yellowstatus = False
    purplestatus = False
    global counter
    counter = 0

def massanalyze():
    while bluestatus == False or redstatus == False or greenstatus == False or yellowstatus == False or purplestatus == False:
        drawnlots()
        global counter
        counter+= 1
#def draw():
    #drawnumber = random.randint(0,1000)
    #return drawnumber
    ''' retired method: incorporated into drawnlots()'''
def testkeylist():
    print(setup())
    '''test method'''
if __name__ == '__main__':
    globalreset()
    setup()
    #print(globalkeylist)
    massanalyze()
    print("it took " +str(counter) + " tries to pull each colored stick at least once")