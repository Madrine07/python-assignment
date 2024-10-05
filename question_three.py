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
subject_mark = int(input("Enter the mark scored: "))
if subject_mark >= 90:
     print("Grade A")
elif subject_mark >= 80:
     print("Grade B")
elif subject_mark>=70:
     print("Grade C")
elif subject_mark >=60:
     print("Grade D")
elif subject_mark >= 50:
     print("Grade E")
else:
    print("Fail")



 