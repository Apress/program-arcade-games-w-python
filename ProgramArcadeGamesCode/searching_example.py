# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

# --- Read in a file from disk and put it in an array.
file = open("super_villains.txt")

name_list = []
for line in file:
    line = line.strip()
    name_list.append(line)

file.close()

# --- Linear search
key = "Morgiana the Shrew"
 
i = 0
while i < len(name_list) and name_list[i] != key:
    i += 1
 
if i < len(name_list):
    print( "The name is at position", i)
else:
    print( "The name was not in the list." )

# --- Binary search
key = "Morgiana the Shrew";
lower_bound = 0
upper_bound = len(name_list)-1
found = False

# Loop until we find the item, or our upper/lower bounds meet
while lower_bound <= upper_bound and not found:
    
    # Find the middle position
    middle_pos = (lower_bound + upper_bound) // 2
    
    # Figure out if we:
    # move up the lower bound, or
    # move down the upper bound, or
    # we found what we are looking for
    if name_list[middle_pos] < key:
        lower_bound = middle_pos + 1
    elif name_list[middle_pos] > key:
        upper_bound = middle_pos - 1
    else:
        found = True

if found:
    print( "The name is at position", middle_pos)
else:
    print( "The name was not in the list." )

