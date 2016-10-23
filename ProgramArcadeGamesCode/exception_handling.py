# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

import sys

# Divide by zero
try:
    x = 5 / 0
except:
    print("Error dividing by zero")
    print(sys.exc_info()[0])

# Invalid number conversion
try:
    x = int("fred")
except:
    print("Error converting fred to a number")
    print(sys.exc_info()[0])

numberEntered = False
while not numberEntered:
    numberString = input("Enter an integer: ")
    try:
        n = int(numberString)
        numberEntered = True
    except:
        print("Error, invalid integer")

# Error opening file
try:
    f = open('myfile.txt')
except:
    print("Error opening file")

# Multiple errors
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    x = 101/i
except IOError:
    print("I/O error")
except ValueError:
    print("Could not convert data to an integer.")
except ZeroDivisionError:
    print("Division by zero error")
except:
    print("Unexpected error:", sys.exc_info()[0])


# Generating exceptions
def get_input():
    user_input = input("Enter something: ")
    if len(user_input) == 0:
        raise IOError("User entered nothing")

get_input()
