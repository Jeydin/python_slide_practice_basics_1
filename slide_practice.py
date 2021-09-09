# This is a comment
# Name: Jeydin Pham
# Python Basics Slide Practice (Notes)

print("This is our slide_practice file.")

# Blank line
print()


print("This is line 11.")

# Changing the end
print("Hello, World", end = " === ")

# Escape Sequences always start with \

print("My poem is titled \"My Haiku\" and it's great.")

# Escape Sequences List
# \" - displays a double quote in a print statement
# \' - displays a single quote in a print statement
# \t - tabs over
# \n - move to the next line
# \r - prints over the beginning of the license
# \\ - prints a backslash

print("Here is the first line\nHere is my second line")

# Variables
grade = 95
# Storing 95 into variable "grade"
student = "Mr. P"
# Storing a string to "student"
check = True
# Boolean is a variable that holds True of False

# Other types of variables
# Integer (whole number)
# Float (decimal number, ex. 4.5)
# String (group of characters, in quotations)
# List (lots of variables in a list)

# Indentifier 
# Do not use random variable names

grade = 90
x = 90

# Naming your variables with a useful name

# Case Sensitivity 
# Name is not the same as name
# Name is not the same as NAME
NAME = "Tony"
Name = "Tony"
name = "Tony"

# Convert from String to a Number

userinput = "33"
usernum = int(userinput)
print(3 * usernum)

# User Input 

name = input("What is your name? \n")
print("Your name is", name)
# Comma connectors add a space for us

num = input("What is your number? \n")
print("Your number is", num)

# Strings & Numbers
numString = "56"
print(4 + int(numString))

# Math Operators
# (experssion) - tells the computer to do this first
# ** - exponents (2 ** 5, two to the fifth power)
# -x = negation (changes sign)
# * - is multiply
# / - is division
# % - modulus (finds remainder)
# 10 % 3 = 1, because 10 / 3 = 3 with 1 left over
# +, - = addition, subtraction

first = 2
second = 3
third = 10
fourth = 20
fifth = 3

total = first + second + third
product = fourth * fifth

# // - floor division (two forward slashes)
# aka integer division

int_div = 75 // 12
print("Integer division is", int_div)


# Regular division
dec1 = 4 / 4.0
dec2 = 3 / 4
print("Answer 1 is", dec1)
print("Answer 2 is", dec2)

# Shortcut operators

num1 = 5
num2 = 4
num3 = 3

num3 = num3 + 1
num3 += 1 # Shortcut addition

num2 = num2 * 2
num *= 2 # Multiply shortcut (num2 * 2)