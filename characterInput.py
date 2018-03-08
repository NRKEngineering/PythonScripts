# Character input
# This program asks for the users name and age and then calculates
# what the year they turn 100 years old.

# import modules
import datetime
s
# Get name
name = input("What is your name?: ")
# Get age
age = input("What is your age?: ")

print ("Your name is " + name + " and you are " + age + " years old")

# get current year
now = datetime.datetime.now()
year = now.year

# Calculate when user is 100 years old
century = 100 - int(age) + year

print ("You will be 100 in the year " + str(century))
