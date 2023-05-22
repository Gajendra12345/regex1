                           #-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      in
#
# Created:     03-05-2023
# Copyright:   (c) in 2023
# Licence:     <your licence>
#-----------------------------------------------------------------------------
final_result = []

def getDivision(student_name,student_marks):
    if len(student_name) == len(student_marks):
        flag1,flag2 = False,False

        for name in student_name:
            if type(name) == str:
                flag1 = True
            else:
                flag1 = False
                print("Name only acceptable string")
                break

        for mark in student_marks:
            if type(mark) == int or type(mark) == float:
                flag2 = True
            else:
                flag2 = False
                print("marks only acceptable int and float")
                break

        if flag1 == True and flag2 == True:
            for i in range(len(student_name)):
                if student_marks[i] >= 75:
                    final_result.append(student_name[i]+'* :frist Division')
                elif student_marks[i] >= 60 and student_marks[i] < 75:
                    final_result.append(student_name[i]+' :frist Division')
                elif student_marks[i] >= 45 and student_marks[i] < 60:
                    final_result.append(student_name[i]+' :second Division')
                elif student_marks[i] < 45 :
                    final_result.append(student_name[i]+' :failed')
                else:
                    pass
    else:
        print("Length of student names list and student's marks list not equal")


student_name = ['Ram','Rahul','Prakash','Puja']
student_marks = [80,65,50,40]
getDivision(student_name,student_marks)


for result in final_result:
    print(result)








