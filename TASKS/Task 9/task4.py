items_list = ["apple","cherry", "mango", "Milk"]

store = {}

# print("Enter the price of the following items")

for item in items_list:
    while True:
        print("Enter the list of item that you want: ")
        if price.isdigit():   # Input validation (must be number)
            store[item] = int(price)
            break