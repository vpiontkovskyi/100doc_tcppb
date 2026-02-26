"""
A collection of programming exercises designed to practice fundamental Python skills.

The module includes tasks such as printing formatted strings, fixing syntax errors,
and performing variable value swaps. These exercises reinforce core Python concepts like
string manipulation, debugging, and variable assignments.
"""


"""
https://www.udemy.com/course/100-days-of-code/learn/quiz/6113788#overview
Write a program that uses print statements to print the following recipe into the Output console. The text to print 
is already there, you just need to make it into code. Your code should print all five lines exactly the same as the 
example output below. Make sure that you don't change any of these existing text as everything, punctuation and 
casing all need to match!
"""
print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n"
      "2. Knead the dough for 10 minutes.\n"
      "3. Add 3g of Salt.\n"
      "4. Leave to rise for 2 hours.\n"
      "5. Bake at 200 degrees C for 30 minutes.")  # passed

"""
https://www.udemy.com/course/100-days-of-code/learn/quiz/6113868#overview
Look at the code in the code editor. There are errors on all 5 lines of code. Fix the code so that it runs without 
errors. Try to run the code and debug each line using the error messages and feedback.
"""
print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print(r"New lines can be created with a \ and the letter n")  # passed

"""
https://www.udemy.com/course/100-days-of-code/learn/quiz/6113876#overview
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch 
the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use 
variables to solve this exercise.
"""
glass1 = "milk"
glass2 = "juice"
glass1, glass2 = glass2, glass1  # passed
