# -*- coding: utf-8 -*-
"""
Ideas for text Adventure data structures.
"""

# We could use lists.
kitchen = ["Kitchen","This is the kitchen."]
livingRoom = ["Living Room","There's a dusty sofa here."]
bedroom = ["Bedroom","There is a creepy doll here."]

rooms = [kitchen, livingRoom, bedroom]

for room in rooms:
    print("You are in", room[0])
    print("Description:"room[1])
    print()
    print("Moving to the next room...")
    
# We could use dictionaries
    
    
romDict = {
        "Kitchen":"This is the kitchen",
        "Living Room","There's a dusty sofa here.",
        "Bedroom","There's a creepy doll here."
        }