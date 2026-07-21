import numpy as np

# ==========================================
# STUDENT MARKS ANALYSIS SYSTEM
# ==========================================

students = np.array([
    ["Ali", 85, 90, 88],
    ["Ahmed", 72, 68, 75],
    ["Sara", 95, 98, 96],
    ["Ayesha", 60, 55, 58],
    ["Bilal", 80, 79, 85]
], dtype=object)

print("=" * 50)
print("      STUDENT MARKS ANALYSIS SYSTEM")
print("=" * 50)

print("\nStudent Data\n")
print(students)

# ------------------------------
# Separate Names and Marks
# ------------------------------

names = students[:, 0]

marks = students[:, 1:].astype(int)

# ------------------------------
# Total Marks
# ------------------------------

total = np.sum(marks, axis=1)

print("\nTotal Marks")
print(total)

# ------------------------------
# Average Marks
# ------------------------------

average = np.mean(marks, axis=1)

print("\nAverage Marks")
print(np.round(average, 2))

# ------------------------------
# Highest Total
# ------------------------------

highest_index = np.argmax(total)

print("\nTop Student")
print(names[highest_index])
print("Total =", total[highest_index])

# ------------------------------
# Lowest Total
# ------------------------------

lowest_index = np.argmin(total)

print("\nLowest Student")
print(names[lowest_index])
print("Total =", total[lowest_index])

# ------------------------------
# Subject Wise Average
# ------------------------------

subject_average = np.mean(marks, axis=0)

subjects = ["English", "Math", "Science"]

print("\nSubject Wise Average")

for sub, avg in zip(subjects, subject_average):
    print(sub, ":", round(avg, 2))

# ------------------------------
# Highest Marks in Each Subject
# ------------------------------

highest_subject = np.max(marks, axis=0)

print("\nHighest Marks Subject Wise")

for sub, mark in zip(subjects, highest_subject):
    print(sub, ":", mark)

# ------------------------------
# Lowest Marks
# ------------------------------

lowest_subject = np.min(marks, axis=0)

print("\nLowest Marks Subject Wise")

for sub, mark in zip(subjects, lowest_subject):
    print(sub, ":", mark)

# ------------------------------
# Pass Students
# ------------------------------

average = np.mean(marks, axis=1)

passed = average >= 60

print("\nPassed Students")

print(names[passed])

# ------------------------------
# Failed Students
# ------------------------------

failed = average < 60

print("\nFailed Students")

print(names[failed])

# ------------------------------
# Students Above 90 Average
# ------------------------------

excellent = average >= 90

print("\nExcellent Students")

print(names[excellent])

# ------------------------------
# Overall Statistics
# ------------------------------

print("\nOverall Statistics")

print("Overall Average =", np.mean(marks))

print("Highest Mark =", np.max(marks))

print("Lowest Mark =", np.min(marks))

print("Total Marks =", np.sum(marks))

# ------------------------------
# Rank Students
# ------------------------------

rank = np.argsort(total)[::-1]

print("\nRanking")

for i in rank:
    print(names[i], "=", total[i])

print("\nProgram Finished Successfully.")