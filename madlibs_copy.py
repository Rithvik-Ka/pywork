"""
Name: Rithvik Kandula
Date: September 16, 2025
Course: ICS3U1
Project: Lesson 6: Mad Lib Project
"""

#I wrote the story here:
"""Yesterday, I had a quite 0-ADJECTIVE day. 
As soon as I woke up, I realised I was 1-PLACE the 2-THING. 
I was very 3-ADJECTIVE about this, but the day was just about 
to get more 4-ADJECTIVE. 
I got up and put on my 5-CLOTHES and 6-CLOTHES, not 7-ADJECTIVE 
about what I was wearing. 
I went downstairs to meet my 8-ADJECTIVE parents and had 9-NUMBER * 
2 10-FOOD for breakfast.
I 11-ADJECTIVELY ate my breakfast and 12-VERB outside.
As I was 13-VERB to my school bus, I was 14-ADJECTIVE because 
15-PERSON was 16-VERB at me.
Little did I know it was because of my 17-THING"""
from formatting import clr
#Intro
input('\n'*21 + "Welcome to Rithvik's Madlib!")
print("\n"*21)

#storing all the variables in order that they appear in the paragraph
wrds = {"adjective1": clr.red(input("Enter an adjective: ")), 
        "preposition1": clr.red(input("Enter a preposition(on, in, under, etc.): ")), 
        "thing1": clr.red(input("Enter a thing(something that would be in a house): ")), 
        "adjective2": clr.red(input("Enter an adjective: ")), 
        "adjective3": clr.red(input("Enter an adjective: ")), 
        "clothes1": clr.red(input("Enter a type of shirt(hoodies, jackets, etc.): ")), 
        "clothes2": clr.red(input("Enter a type of pant(shorts, sweats, etc.): ")), 
        "adjective4": clr.red(input("Enter an adjective: ")), 
        "adjective5": clr.red(input("Enter an adjective(for a person): ")), 
        "number1": clr.red(str(2*int(input("Enter a number: ")))), 
        "food1": clr.red(input("Enter a food: ")), 
        "adjective6": clr.red(input("Enter an adjective(ending with 'ly'): ")), 
        "verb1": clr.red(input("Enter a verb(endign in 'ed'): ")),
        "verb2": clr.red(input("Enter a verb(movign a distance, ending in 'ing'): ")),
        "adjective7": clr.red(input("Enter an adjective: ")), 
        "person1": clr.red(input("Enter a person: ")), 
        "verb3": clr.red(input("Enter an verb(endign in 'ing'): ")), 
        "thing2": clr.red(input("Enter a thing: "))}

#printing:
print("\n\n\n\n\n------THE STORY------\nYesterday, I had a quite", 
wrds["adjective1"], "day.\n"+
"As soon as I woke up, I realised I was", wrds["preposition1"], "the", wrds["thing1"] +".\n"+
"I was very", wrds["adjective2"], "about this, but the day was just about to get more",
 wrds["adjective3"] + ".\n"+ 
"I got up and put on my", wrds["clothes1"], "and", wrds["clothes2"] + ", not", wrds["adjective4"], 
"about what I was wearing.\n"+
"I went downstairs to meet my", wrds["adjective5"], "parents and had", wrds["number1"], 
wrds["food1"],
 "for breakfast.\n"+
"I", wrds["adjective6"], "ate my breakfast and", wrds["verb1"], "outside.\n"+
"As I was", wrds["verb2"], "to my school bus, I was", wrds["adjective7"], "because", 
wrds["person1"], "was", wrds["verb3"], "at me.\n"+
"Little did I know it was because of my", wrds["thing2"] + 
".\n------THE END!------")