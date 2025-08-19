'''
**Task6**

- The Federal Government of Nigeria has set the minimum age for admission into federal tertiary institutions at 16 years old for the 2025/2026 academic session, according to the Minister of Education, Dr. Tunji Alausa. This policy, announced at the 2025 JAMB policy meeting, replaces the previous 18-year minimum age requirement. 

- For the 2025/2026 academic session, the University of Lagos (UNILAG) requires candidates to have a minimum UTME score of 200 to be eligible for the Post-UTME screening. The Post-UTME itself is an online screening exercise. UNILAG does not release specific departmental cut-off marks before the screening. The departmental cut-off marks are determined after the Post-UTME, based on merit and the performance of candidates in both UTME and the Post-UTME. 

Breakdown of the Admission Process:
1. UTME:
Candidates must score 200 or above in the UTME and choose UNILAG as their first choice. 
2. O'Level Requirements:
Candidates must also have five (5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics. 
3. Post-UTME:
Eligible candidates participate in the university's online Post-UTME screening. 
4. Departmental Cut-off Marks:
After the Post-UTME, the university determines departmental cut-off marks based on merit and overall performance
(This can range from 200 to 320). 
5. Final Admission:
Candidates who meet the departmental cut-off marks are offered admission. 

- Write a program to account for all of the conditions above, Such that when a user imputes all their required details, they are told if they will be legible for admission or not.
'''

# Minimum age (must be 16 or above)

# UTME score (must be 200 or above)

# UNILAG must be first choice

# O'Level requirements: at least 5 credit passes at one sitting, including Math and English

# Post-UTME screening score

# Checks if combined UTME and Post-UTME meets assumed departmental cut-off (mocked)

name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
utme_score = int(input("Enter your UTME score (out of 400): "))
first_choice = input("Did you choose UNILAG as your first choice? (yes/no): ").lower()
olevel_credits = int(input("How many credit passes do you have at ONE sitting?: "))
eng_math = input("Do you have credits in both English Language and Mathematics? (yes/no): ").lower()
post_utme_score = float(input("Enter your Post-UTME score (0 - 100): "))
dept_cut_off = int(input("Enter your departmental cut-off mark (200-320): "))

average_score = utme_score + post_utme_score /2
print(average_score)

age_allowed = age >= 16
utme_allowed = utme_score >= 200
olevel_credits_allowed = olevel_credits >= 5
first_choice_allowed = first_choice == first_choice
cut_off_allowed = average_score >= dept_cut_off

eligibility = (age_allowed and utme_allowed) and (olevel_credits_allowed and cut_off_allowed)

print(f"\n----- ADMISSION STATUS-----")
print(f"Name: ", name)
print(f"Admission Status: ", eligibility)