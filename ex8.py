###############################################################################
#  Program Name   : ex8.py
#  Author         : Rithvik Kandula
#  Task           : Write a program that keeps asking the user for words until they type exit.
###############################################################################
try:
    from formatting import clr, type

    value = ""
    while value != "exit":
        value = input("Enter a word: ")
    type(clr.red("You typed: ") + clr.brt_green(value))

except:
    value2 = ""
    while value2 != "exit":
        value2 = input("Enter a word: ")
    print("You typed: " + str(value2))