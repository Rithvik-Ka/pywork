###############################################################################
#  Program Name   : ex11.py
#  Author         : Rithvik Kandula
#  Task           : Write a function that takes your name and age as parameters and prints a sentence about you.
###############################################################################
from formatting import clr, type

def about_me(name, age):
    type("My name is "+ clr.red(name) +" and I am "+ clr.brt_green(age)+" years old.")

name = input("Enter your name: ")
age = input("Enter your age: ")
about_me(name, age)