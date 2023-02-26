import random

# Get the user input for the range of the random number.

min_value= int(input("ENTER THE MINIMUM VALUE:"))
max_value=int(input("ENTER THE MAXIMUM VALUE:"))

# Generate a random integer with the given value.

random_int=random.randint(min_value,max_value)

# print the random number

print("Random number between ", min_value, "and" , max_value, "is", random_int)