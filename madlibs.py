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

#Intro
input("\n"*21 + "Welcome to Rithvik's Madlib!")
print("\n"*21)

#storing all the variables in order that they appear in the paragraph
wrds = [input("Enter an adjective: "), 
        input("Enter a preposition(on, in, under, etc.): "), 
        input("Enter a thing(something that would be in a house): "), 
        input("Enter an adjective: "), 
        input("Enter an adjective: "), 
        input("Enter a type of shirt(hoodies, jackets, etc.): "), 
        input("Enter a type of pant(shorts, sweats, etc.): "), 
        input("Enter an adjective: "), 
        input("Enter an adjective(for a person): "), 
        str(2*int(input("Enter a number: "))), 
        input("Enter a food: "), 
        input("Enter an adjective(ending with 'ly'): "), 
        input("Enter a verb(endign in 'ed'): "),
        input("Enter a verb(movign a distance, ending in 'ing'): "),
        input("Enter an adjective: "), 
        input("Enter a person: "), 
        input("Enter an verb(endign in 'ing'): "), 
        input("Enter a thing: ")]

#printing:
print("\n\n\n\n\n------THE STORY------\nYesterday, I had a quite", 
wrds[0], "day.\n"+
"As soon as I woke up, I realised I was", wrds[1], "the", wrds[2] +".\n"+
"I was very", wrds[3], "about this, but the day was just about to get more",
 wrds[4] + ".\n"+ 
"I got up and put on my", wrds[5], "and", wrds[6] + ", not", wrds[7], 
"about what I was wearing.\n"+
"I went downstairs to meet my", wrds[8], "parents and had", wrds[9], 
wrds[10],
 "for breakfast.\n"+
"I", wrds[11], "ate my breakfast and", wrds[12], "outside.\n"+
"As I was", wrds[13], "to my school bus, I was", wrds[14], "because", 
wrds[15], "was", wrds[16], "at me.\n"+
"Little did I know it was because of my", wrds[17] + 
".\n------THE END!------")