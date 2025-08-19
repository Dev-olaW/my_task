"""
Task5: Store Inventory Update**
- Create a dictionary called store with items and their available quantities. Example:
```
store = {"Book": 10, "Pen": 20, "Bag": 5}
```


- Ask the user to input the item they want to buy (e.g., "Pen").

- Ask the user to input the quantity they want to purchase.

- Use the assignment operator -= to update (reduce) the item quantity in the dictionary.

- Print the updated dictionary in this format:

```
Before purchase: {'Book': 10, 'Pen': 20, 'Bag': 5}
After purchase: {'Book': 10, 'Pen': 18, 'Bag': 5}
"""
# Create a dictionary called store with items and their available quantities.

store = dict(Book = 10, Pen= 20, Bag = 5)

items = input("Enter the item that you want to buy: ").title()
quantity = int(input("Enter the quantity that you want to purchase: "))

# Use the assignment operator -= to update (reduce) the item quantity in the dictionary.
store[items] -= quantity

# Print

print (store)