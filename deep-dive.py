# Problem Statement: You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:
# Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

print(students[2], grades[2], activities[2])

print("="*50)
#-------------------------------
# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

students_approved= []
students_approved.append(students[0])
students_approved.append(students[1])
students_approved.append(students[3])

#----------------
# Task 3: Print the list students_approved
print(students_approved)
