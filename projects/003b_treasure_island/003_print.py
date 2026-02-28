"""
A BMI (Body Mass Index) calculator with conditional interpretation.
This module calculates BMI based on the provided weight and height values and
provides an interpretation of the BMI category. It categorizes BMI into
three categories: underweight, normal weight, and overweight.
"""


"""
https://www.udemy.com/course/100-days-of-code/learn/quiz/6449969#content
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
If the bmi is under 18.5 (not including), print out "underweight"
If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
If the bmi is 25 (including) or over, print out "overweight"
"""
weight = 85
height = 1.85
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("underweight")
elif 15 <= bmi <= 25:
    print("normal weight")
elif bmi > 25:
    print("overweight")  # passed
