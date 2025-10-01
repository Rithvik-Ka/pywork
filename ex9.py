###############################################################################
#  Program Name   : ex9.py
#  Author         : Rithvik Kandula
#  Task           : Write a program that prints all odd numbers from 1 to 19.
###############################################################################
from formatting import clr, type

for i in range(20):
    if i % 2 != 0:
        type(clr.brt_green(str(i)))