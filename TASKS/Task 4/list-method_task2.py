# Create an empty list 
empty_list = []

# Ask user to enter 3 shopping items (one by one)

items = ([ 
    input("Enter the first shopping items: "), 
    input("Enter the first shopping items: "), 
    input("Enter the first shopping items: ")
    ])

# Add them to the list.
empty_list.extend(items)

# Display the list as a single string, separated by commas.

print(empty_list)