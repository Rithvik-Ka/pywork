###############################################################################
#  Program Name   : ex10.py
#  Author         : Rithvik Kandula
#  Task           : Write a program that asks for 3 friends’ names, stores them in a list, and prints them all.
###############################################################################
try:
    from formatting import clr, type
    friends = [input("Enter friend number 1: "), input("Enter friend number 2: "), input("Enter friend number 3: ")]
    type("Your friends are:\n"+ clr.red(friends[0]) + ", "+ clr.brt_blue(friends[1])+ ", and "+ clr.brt_green(friends[2]))

except:
    friends = [input("Enter friend number 1: "), input("Enter friend number 2: "), input("Enter friend number 3: ")]
    print("Your friends are:\n"+ str(friends[0]) + ", "+ str(friends[1])+ ", and "+ str(friends[2]))