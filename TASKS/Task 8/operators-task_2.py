# Task 2

# comment bthe code below approipriately

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

''''
The code above ask user to enter name, age, and test score to check for eligibility.
Age must be less than 18 and the test score must be avove 70.l
The result shows that the canditate is above 18 and the test score is less thn 70, which make the user not eligible.
'''

# 2. Adapt the code to the case
'''- Adapt the code to the case below.

- Federal Government Scholarship Key Eligibility Requirements:
  - Citizenship:
    - Applicant must be a citizen of Nigeria. 
  - Enrollment:
    - Must be a registered, full-time undergraduate student in a recognized Nigerian university. 
  - Other Scholarships:
    - Applicants cannot be currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international. 
  - Academic Qualification:
    - For undergraduate courses, applicants usually need five distinctions (As and Bs) in relevant subjects in their WAEC/WASSCE (May/June) exams, including English and Mathematics.
    '''

# FEDERAL GOVERNMENT SCHOLARSHIP ELIGIBILITY
name = input("Applicant name: ").title()
institution = input("Enter the name of your University: ").title()
citizenship = input("Are you a citizen of Nigeria (yes/no): ").lower()
enrollment_status = input("Are you a registered, full-time undergraduate student in a recognized Nigerian university? (yes/no): ").lower()
other_schorlarships_status = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, whether national or international? (yes/no): ").lower()


Mathematics = input("Score for Mathematics (A,B,C,D,E or F): ").upper()
English = input("Score for English (A,B,C,D,E or F): ").upper()
other_qualification = input("Do you have at least three distinction in other relevant subjects in WAEC/WASSCE exams(yes/no): ").lower()
    

eligibility = (citizenship == "yes" and  enrollment_status == "yes" and other_schorlarships_status == "no" and other_qualification == "yes") and (Mathematics == "A" or Mathematics == "B") and (English == "A" or English == "B")

print(f"\n----- SCHOLARSHIP STATUS-----")
print(f"Name: ", name)
print(f"Citizenship status: ", citizenship)
print (f"Name of University: ", institution)
print(f"Admission Status: ", eligibility)