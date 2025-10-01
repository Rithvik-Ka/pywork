###############################################################################
#  Program Name   : ex7.py
#  Author         : Rithvik Kandula
#  Task           : Write a program that asks for two numbers and prints the larger one.
###############################################################################
try:
    from formatting import clr, type

    thing = [int(input(("Number1: "))), int(input("Number2: "))]
    thing.sort()
    type("Your numbers listed are:\n"+ clr.red(str(thing[0]))+" "+ clr.green(str(thing[1])))

except:
    thing2 = [int(input(("Number1: "))), int(input("Number2: "))]
    thing2.sort()
    print("Your numbers listed are:\n"+ str(thing2[0])+" "+ str(thing2[1]))