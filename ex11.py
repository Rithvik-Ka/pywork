###############################################################################
#  Program Name   : ex11.py
#  Author         : Rithvik Kandula
#  Task           : Write a function that takes your name and age as parameters and prints a sentence about you.
###############################################################################
try:
    from formatting import clr, type
    def about_me(name, age):
        type("My name is "+ clr.red(name) +" and I am "+ clr.brt_green(age)+" years old.")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    about_me(name, age)

except:
    def about_me(name, age):
        print("My name is "+ str(name) +" and I am "+ str(age)+" years old.")

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    about_me(name, age)