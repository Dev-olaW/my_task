# Task 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1 = 4
num2 = 5

print(f"{num1} == {num2} : {num1 == num2}") ## 4 == 5:False
# Output is False because the input (num1 = 4) is not equal to (num2 =5)

print(f"{num1} != {num2} : {num1 != num2}") #  4 != 5
# Output is True because the results shows that input (num1 = 4) is not equal to (num2 =5)

print(f"{num1} > {num2} : {num1 > num2}") # 4 > 5 : False
# Output is Flase becuse num1 is not greater than num 2

print(f"{num1} < {num2} : {num1 < num2}") # 4 < 5 : True
# Output is true because num1 is less than num2

# USECASE AND SCENARIOS
# 1. Voting Eligibility     2. Admission Eligibility    3. Exam result

# A code on one of the 3 cases

# EXAM RESULTS

exam_result = int(input("Enter your exam result: "))


print("Passed: ", exam_result >= 40)



