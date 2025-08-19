'''**Task4: Student Record**
- Create an empty dictionary called student.

- Ask the user to input their name and age, then store them in the dictionary.

- Add a list of scores (e.g., [70, 85, 90]) to the dictionary.

- Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

- Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".

- Print out the complete record in this format:

```
Student Record:
Name: John
Age: 16
Scores: [70, 85, 90]
Passed: True
Teenager: True
'''

# Create an empty dictionary called student.
student = {}


# - Ask the user to input their name and age, then store them in the dictionary.
 
name = input("Enter your name: ")
age = int(input("Enter your age: "))

student = {"name": name, "age": age}
print(student)

# Add a list of scores (e.g., [70, 85, 90]) to the dictionary.
score1 = 30
score2 = 85
score3 = 90

scores = (score1, score2, score3)
scores = [scores]
student["scores"] = [30, 85, 90]

print(student)

# print(student)

# #  Use a comparison operator to check if the student has passed (average score >= 50). Save the result (True/False) in the dictionary under the key "passed".

status = (score1 >= 50)
student = {"scores": scores, "Passed": status}
print(student)

status = (score2 >= 50)
student = {"scores": scores, "Passed": status}
print(student)

status = (score3 >= 50)
student = {"scores": scores, "Passed": status}
print(student)

# Use a logical operator to check if the student is a teenager (age between 13 and 19). Save the result as "teenager".
Teenager = (age >= 13 and age <= 19)

print(f"\n----STUDENT RECORD------")
print(f"Name:", name)
print(f"Age:", age)
print(f"Scores:", scores)
print(f"Passed:", status)
print(f"Teenager:", Teenager)