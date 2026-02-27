"""
A calculator program to split a bill and tip among a group of people.
This program calculates the total bill per person, including tip and divides
it among the specified number of people. Input validation is used to ensure
the bill, tip, and number of people are correctly entered.
"""


"""
Shorter version and as expected in course.
"""
# print("Welcome to the Tip Calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
# people = int(input("How many people to split the bill? "))
# total_tip = bill * (tip / 100)
# total_bill = bill + total_tip
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${bill_per_person}")


"""
As upgrade of this program I propose add validation to input: non empty, non spaces, entity specific checks.
"""
def read_bill(prompt: str) -> float:
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                raise ValueError("input cannot be empty")
            value = float(raw)
            if value <= 0:
                raise ValueError("bill must be greater than 0")

            return value
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def read_tip(prompt: str) -> int:
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                raise ValueError("input cannot be empty")
            value = int(raw)
            if value <= 0:
                raise ValueError("tip must be greater than 0")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def read_people(prompt: str) -> int:
    while True:
        try:
            raw = input(prompt).strip()
            if not raw:
                raise ValueError("input cannot be empty")
            value = int(raw)
            if value < 1:
                raise ValueError("people must be >= 1")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

print("Welcome to the Tip Calculator!")
bill = read_bill("What was the total bill? $")
tip = read_tip("How much tip would you like to give? ")
people = read_people("How many people to split the bill? ")
bill_per_person_rounded = round((bill + (bill * (tip / 100))) / people, 2)
print(f"Each person should pay: ${bill_per_person_rounded}")
