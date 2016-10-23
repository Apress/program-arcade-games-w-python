file = open("example_sorted_names.txt")
line_list = file.readlines()
file.close()

print("There were", len(line_list), "lines in the file.")
for line in line_list:
    print(line)
