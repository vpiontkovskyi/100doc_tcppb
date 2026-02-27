"""
A script to calculate and display the Body Mass Index (BMI) based on a person's height and weight.

The BMI is calculated using the formula: weight divided by the square of the height. This program
outputs both the raw BMI value and a rounded version for improved readability.
"""


"""
https://www.udemy.com/course/100-days-of-code/learn/quiz/6447301#content
The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is 
the formula used to calculate it: bmi is equal to the person's weight divided by the person's height squared.
"""
height = 1.65
weight = 84
bmi = weight / (height ** 2)
print(bmi)  # passed

bmi = round(weight / (height ** 2), 2)  # rounded to 2 for human readability
print(f"Height = {height}, Weight = {weight}, BMI = {bmi}")  # added f-string
