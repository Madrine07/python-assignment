# WITI has tasked you to automate a simple grading system. As a python student, 
# write a program using operators to display the grades that the students will be receiving based
# on the mark scored in a subject.
# 90% - 100%   Grade is A
# 80% - 89%    Grade is B
# 70% - 79%    Grade is C
# 60% - 69%    Grade is D
# 50% - 59%    Grade is E
# < 50%        Fail
# SOLUTION
# subject_mark = int(input("Enter the mark scored: "))
# if subject_mark >= 90:
#     grade = "A"
# elif subject_mark >= 80:
#     grade = "B"
# elif subject_mark>=70:
#     grade = "C"
# elif subject_mark >=60:
#     grade = "D"
# elif subject_mark >= 50:
#     grade = "E"
# else:
#     grade = "Fail"
# print("Grade:", grade)

# OR
def calculate_grades():

    print("\n...Student Grade Calculations...")

    mark = int(input("Enter the subject mark: \t"))
    if mark >= 90 and mark<= 100:
        print('Grade is A')
    elif mark >= 80 and mark <= 89:
        print ("Grade is B")
    elif mark >= 70 and mark <= 79:
        print('Grade is C')
    elif mark >= 60 and mark <= 69:
        print('Grade is D')
    elif mark >= 50 and mark <= 59:
        print('Grade is E')
    else:
        print('Fail')
calculate_grades()     #Calling the function



 