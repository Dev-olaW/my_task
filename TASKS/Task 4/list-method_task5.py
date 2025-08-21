#  Ask the user for 3 student names.
empty_list1 = []
empty_list2 = []


student_name = ({
input("Enter the first student's name: "),
input("Enter the second student's name: "),
input("Enter the third student's name: ")
})

# For each student, ask for their score.
scores = ([
    int(input("Enter the first student's score: ")),
    int(input("Enter the second student's score: ")),
    int(input("Enter the trhird student's score: "))
])

# Store the results in two lists (one for names, one for scores).
name_list = empty_list1.extend(student_name)
score_list = empty_list2.extend(scores)


# Print a formatted output showing Name — Score
print("\nStudent Scores:")

