while True:
    print("Hello World!")
# the space between pGCXHCkHsad 
# 
# 
# 
# 
# sdnfgasdfnaskdjflasdjflasjdflasjdfklsjdfkldjasfljasdkfljasdlkfjsadklfjasdfjkldsfdsfdsfdsfdsfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfwhile True:
    print("What is your name?")
    name = input()
    if name != 'Sami':
        continue
    else: print("Welcome Sami! What is your password? (it's a fish)")
    password = input()
    if password == 'swordfish':
        break
print ("Access Granted")

#range(12, 16) - 12, 13, 14, 15
#range(0, 10, 2) - 0, 2, 4, 6, 8
#range(5, -1, -1) - 5, 4, 3, 2, 1, 0 

##importing modules

#The random.randint() function call evaluates to a random integer value between the two integers that you pass it.

#  from random import *.
# With this form of import statement, calls to functions in random will not 
# need the random. prefix. However, using the full name makes for more read
# able code, so it is better to use the normal form of the import statement.

#import random, sys, os, math

## ending a Program early with sys.exit()

import sys
while True:
    print('type exit to exit the program.')
    response = input()
    if response == 'exit':
        sys.exit()
    else: print('your response'+ response + '.')
