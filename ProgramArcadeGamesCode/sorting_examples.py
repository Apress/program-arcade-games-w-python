# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/

import random


def selection_sort(list):
    """ Sort a list using the selection sort """

    # Loop through the entire array
    for cur_pos in range(len(list)):
        # Find the position that has the smallest number
        # Start with the current position
        min_pos = cur_pos

        # Scan left to right (end of the list)
        for scan_pos in range(cur_pos + 1, len(list)):

            # Is this position smallest?
            if list[scan_pos] < list[min_pos]:

                # It is, mark this position as the smallest
                min_pos = scan_pos

        # Swap the two values
        temp = list[min_pos]
        list[min_pos] = list[cur_pos]
        list[cur_pos] = temp


def insertion_sort(list):
    """ Sort a list using the insertion sort """

    # Start at the second element (pos 1).
    # Use this element to insert into the
    # list.
    for key_pos in range(1, len(list)):

        # Get the value of the element to insert
        key_value = list[key_pos]

        # Scan from right to the left (start of list)
        scan_pos = key_pos - 1

        # Loop each element, moving them up until
        # we reach the position the
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1

        # Everything's been moved out of the way, insert
        # the key into the correct location
        list[scan_pos + 1] = key_value


# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.
def print_list(list):
    for item in list:
        print("{:3}".format(item), end="")
    print()

# Create two lists of the same random numbers
list1 = []
list2 = []
list_size = 10
for i in range(list_size):
    new_number = random.randrange(100)
    list1.append(new_number)
    list2.append(new_number)

# Print the original list
print_list(list1)

# Use the selection sort and print the result
print("Selection Sort")
selection_sort(list1)
print_list(list1)

# Use the insertion sort and print the result
print("Insertion Sort")
insertion_sort(list2)
print_list(list2)
