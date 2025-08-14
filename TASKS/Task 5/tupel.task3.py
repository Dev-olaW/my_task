# Asking Users for name of Nigerian State state
User_1 = input("Enter a Nigerian State: ")
User_2 = input("Enter a Nigerian State: ")
User_3 = input("Enter a Nigerian State: ")
User_4 = input("Enter a Nigerian State: ")
User_5 = input("Enter a Nigerian State: ")
Nigerian_State = (User_1, User_2, User_3, User_4, User_5)

# Printing tht e first and last state
print(Nigerian_State[0])
print(Nigerian_State[-1])

# Check if "Lagos" is in tuple
Nigerian_State = tuple(Nigerian_State)
print("Lagos" in Nigerian_State)

# Print number of states entered
print(len(Nigerian_State))