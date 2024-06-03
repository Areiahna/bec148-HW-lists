#Task 1: Given the list of grades:
# Sort the grades in descending order and display the sorted list.


grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

grades.sort(reverse=True)
print(grades)

# ---------------------------------------
# Task 2: Calculate the average grade and display it.

total = sum(grades)
average = total / len(grades)
print ("Grade average:", average)

# ---------------------------------------
# Task 3: Replace any grade below 80 with the value Failed.

for x in range(len(grades)):
    if (grades[x] < 80):
        grades[x] = "Failed"
        
print(grades)

