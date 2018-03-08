# Odd or Even
# This program asks the user for a number and
# determines if that number is odd or even

# get a number from the user
number = input("Please enter a number: ")

# See if even
if int(number) % 2 is 0:
    print ("Number is even")
    # If even is it divisable by four
    if int(number) % 4 is 0:
        print ("and is divsible by 4")

# See if odd
elif int(number) % 2 is not 0:
    print ("Number is odd")

# Error check
else:
    print ("Error")
