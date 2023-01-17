"""
Project - Mad Libs Generator
Author - Kushagra Mittal
Date - 17th January 2023

Concepts = Input, Concatenation, String Manipulation
"""

FOREIGN_COUNTRY = input("Enter a Foreign Country: ")
ADVERB_1 = input("Enter an adverb: ")
ADJECTIVE_1 = input("Enter an adjective: ")
ANIMAL = input("Enter an Animal: ")
VERB_ENDING_IN_ING_1 = input("Enter a verb ending in -ing: ")
VERB_1 = input("Enter a verb: ")
VERB_ENDING_IN_ING_2 = input("Enter a verb ending in -ing: ")
ADVERB_2 = input("Enter an adverb: ")
ADJECTIVE_2 = input("Enter an adjective: ")
A_PLACE = input("Enter a place: ")
TYPE_OF_LIQUID = input("Enter a type of liquid: ")
BODYPART = input("Enter a bodypart: ")
VERB_2 = input("Enter a verb: ")
print("\n")


print(
    f"If you're travelling in {FOREIGN_COUNTRY} and find yourself having to cross a Piranha-filled river, here's how to do it {ADVERB_1}:"
    f"\n - Piranhas are more {ADJECTIVE_1} during the day, so cross the river at night."
    f"\n - Avoid areas with netted {ANIMAL} traps---Piranhas may be {VERB_ENDING_IN_ING_1} there looking to {VERB_1} them!"
    f"\n - When {VERB_ENDING_IN_ING_2} the river, swim {ADVERB_2}. You don't wanna wake them up and make them {ADJECTIVE_2}."
    f"\n - Whatever you do, if you have an open wound, try to find another way to get back to the {A_PLACE}. Piranhas are attracted to fresh {TYPE_OF_LIQUID} and will most likely take a bite out of your {BODYPART} if you {VERB_2} in the water!"
)

