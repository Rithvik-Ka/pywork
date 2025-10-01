###############################################################################
#  Program Name   : ex8.py
#  Author         : Rithvik Kandula
#  Task           : Write a program that keeps asking the user for words until they type exit.
###############################################################################
from formatting import clr, type

value = ""
while value != "exit":
    value = input("Enter a word: ")
type(clr.red("You typed: ") + clr.brt_green(value))