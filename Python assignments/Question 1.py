def average(a, b , c):
    return (a+b+c)/3

def grade(num):
    if num>= 80:
        return "grade A"
    elif num >=60:
        return "grade B"
    elif num >= 40:
        return "grade C"
    else:
        return "FAIL"

def total(a, b,c):
   return a+b+c
    
def student_result():
    name= input("Enter student name : ")
    marks1=int(input("Enter first marks :"))
    marks2=int(input("Enter second marks :"))
    marks3=int(input("Enter third marks :"))
    avg=average(marks1, marks2,marks3)
    print(f"Student Name: {name}\nTotal: {total(marks1,marks2, marks3)}\nAverage: {avg}\nGrade: {grade(avg)}")

student_result()