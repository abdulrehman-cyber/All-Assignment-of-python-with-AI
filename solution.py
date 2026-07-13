# def average(a, b, c):
#     return (a + b + c) / 3


# def student_result():

#     name = input("Enter name: ")

#     m1 = int(input("Enter marks 1: "))
#     m2 = int(input("Enter marks 2: "))
#     m3 = int(input("Enter marks 3: "))

#     avg = average(m1, m2, m3)

#     print("Name:", name)
#     print("Average:", avg)

#     if avg >= 80:
#         print("Grade: A")

#     elif avg >= 60:
#         print("Grade: B")

#     else:
#         print("Fail")


# student_result()



# solution 2
def average(a, b, c):
    return (a + b + c) / 3

def grade(num):
    if num >= 80:
        return "Grade A"
    elif num >= 60:
        return "Grade B"
    elif num >= 40:
        return "Grade C"
    else:
        return "FAIL"

def total(a, b, c):
    return a + b + c

def student_result():
    name = input("Enter student name: ")

    marks1 = int(input("Enter first marks: "))
    marks2 = int(input("Enter second marks: "))
    marks3 = int(input("Enter third marks: "))
    print("Total Marks :", total(marks1, marks2, marks3))
    avg = average(marks1, marks2, marks3)
    print("Average:", avg)

    print("Grade:", grade(avg))

student_result()