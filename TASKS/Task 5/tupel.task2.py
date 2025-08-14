# Question 2
User_1 = input("Enter your best friend's name: ")
User_2 = input("Enter your best friend's name: ")
User_3 = input("Enter your best friend's name: ")
User_4 = input("Enter your best friend's name: ")
User_5 = input("Enter your best friend's name: ")
bestfriend_name = (User_1, User_2, User_3, User_4, User_5)
bestfriend_name = tuple(bestfriend_name)

print(bestfriend_name[::-1])