"""
A simple program to generate a band name based on user input.

This program takes the name of the city where the user grew up and the
name of their pet to create a potential band name. It outputs the
generated band name to the console.

Live demo https://appbrewery.github.io/python-day1-demo/
"""


print("Welcome to the Band Name Generator")
city_name = input("What`s the name of the city you grew up in?\n")
pet_name = input("What`s pet`s name?\n")
print(f"Your band name could be {city_name} {pet_name}")
