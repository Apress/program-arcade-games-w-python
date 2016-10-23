# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# Explanation video: http://youtu.be/JK5ht5_m6Mk

# Calculate Miles Per Gallon
print("This program calculates mpg.")

# Get miles driven from the user
miles_driven = input("Enter miles driven:")
# Convert text entered to a
# floating point number
miles_driven = float(miles_driven)

# Get gallons used from the user
gallons_used = input("Enter gallons used:")
# Convert text entered to a
# floating point number
gallons_used = float(gallons_used)

# Calculate and print the answer
mpg = miles_driven / gallons_used
print("Miles per gallon:", mpg)
