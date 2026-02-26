"""
A simple program to generate a band name based on user input.

This program takes the name of the city where the user grew up and the
name of their pet to create a potential band name. It outputs the
generated band name to the console.

Live demo https://appbrewery.github.io/python-day1-demo/
"""

"""
Shorter version and as expected in course.
"""
# print("Welcome to the Band Name Generator")
# city_name = input("What's the name of the city you grew up in?\n")
# pet_name = input("What`s pet`s name?\n")
# print(f"Your band name could be {city_name} {pet_name}")


"""
As upgrade of this program I propose add validation to input: non empty, non spaces, min 2 simbols length.
"""
def validated_input(prompt: str) -> str:
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("The input cannot be empty or consist only of spaces")
            if len(value) < 2:
                raise ValueError("Minimum length is 2 characters")
            return value
        except ValueError as e:
            print(f"Input error: {e}. Please try again.\n")

print("Welcome to the Band Name Generator")
city_name = validated_input("What`s the name of the city you grew up in?\n")
pet_name = validated_input("What`s pet`s name?\n")
print(f"Your band name could be {city_name} {pet_name}")
