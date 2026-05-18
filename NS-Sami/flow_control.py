while True:
    print("Hello World!")
# the space between print is known as indentation. 
# ctrl-C generates a keyboard interrupt and stops the infinite loop.


while True:
    print("What is your name?")
    name = input()
    if name != 'Sami':
        continue
    else: print("Welcome Sami! What is your password? (it's a fish)")
    password = input()
    if password == 'swordfish':
        break
print ("Access Granted")




