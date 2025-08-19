# **Task3: Online Store Cart Calculation**

# - Create a list of items (e.g., "Book", "Pen", "Bag") and another list of prices (e.g., 500, 100, 2000).

# - Start with an empty cart total (cart_total = 0).

# - Use assignment operators (+=) to add the price of some items into cart_total.

# - Print the list of items and the total price using an f-string like this:

# ```
# List of items
items = ["Book", "Pen", "Bag"]

# List of prices
price = [100, 200, 300]

cart_total = 0
cart_total += price[0] 
cart_total += price[1]
cart_total += price[2]


# - Print the list of items and the total price using an f-string 
print(f"Items: {items}")
print(f"Total price : {cart_total}")