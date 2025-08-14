# User's shoppings list
 # # Ask the user to enter three items
item_1 = input("Enter the first item for your shopping list: ")
item_2 = input("Enter the second item for your shopping list: ")
item_3 = input("Enter the third item for your shopping list: ")

# Store the items in a tuple
shopping_list = (item_1, item_2, item_3)

# Convert it to a list, then ask for two more items to add.
shopping_list = list(shopping_list)
item_4 =  input("Enter the fourth item for your shopping list: ")
item_5 = input("Enter the fifth item for your shopping list: ")

# Convert back to a tuple and print the updated list

updated_list = (item_1, item_2, item_3, item_4, item_5)
updated_list = tuple(updated_list)

print("Your updated shopping list: " + " | " .join(updated_list))


