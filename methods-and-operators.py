# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:
# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

for x in range(len(submitted)):
   if submitted[x] in attended:
        print("Attended & Submitted:", submitted[x])
        
print("="*50)
#----------------------------------------------

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

print("Identical :", submitted == attended)
# print("Identical :",submitted is attended)

print("="*50)
#----------------------------------------------
# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

# print(attended)
attended.pop(1)
attended.pop(2)
print(attended)
