# User's Info
name = input("Enter your first name: ")
age = int(input("Enter your age: "))
color = input("Enter your favorite color: ")
town = input("Enter your home town: ")

user_info = (name, age, color, town)
info = tuple(user_info)
name, age, color, town = user_info

print(f"First Name:\t\t{name}")
print(f"Age:\t\t\t{age}")
print(f"Favorite color:\t\t{color}")
print(f"Home Town:\t\t{town}")


