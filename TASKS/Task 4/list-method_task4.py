# Ask the user to enter 5 names (separated by spaces)
name = input(" Enter 5 names \"separate each with space\": ")

# Convert all names to lowercase.
the_name = name.lower()

# Sort the list alphabetically.
name_list = the_name.split(" ")
name_list.sort()

#  Display them one name per line.
print(name_list)
for name in range(len(name_list)):
    print(name_list[name])