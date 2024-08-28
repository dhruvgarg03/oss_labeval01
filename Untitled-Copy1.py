#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

print(np.arange(0,10))


# In[2]:


import numpy as np

print(np.arange(0,10))


# In[4]:


students = {}
type(students)


# In[28]:


students = {}
def add_student():
    studentId = input("Enter studentsID")
    name = input("Enter name")
    student_class = input("Enter class")
    list =[]
    students[studentId] = {'name': name,'class': student_class,'grades': list, 'average':0}

    
def update_grades():
    studentId = input("Enter student Id")
    if studentId in students:
        grades = input("Enter new grades")
        students[studentId]['grades'].append(grades)
    else:
        print("Student not found")

        
        
def calculate_average(studentId):
    
    if studentId in students:
        grades = students[studentId]['grades']
        average = int(sum(grades)/len(grades))
        print("Average of grade is : ",average)
    else:
        print("student not found")
        
def generate_top_students_report():
    for studentId in students:
        average = calculate_average(studentId)
        students[studentId]['average'].append(average)
#     for classId in students:
#         students['class']
def print_students():
    print(students)

    
    
add_student()
add_student()
update_grades()
print_students()
studentId  = input("Enter the studentId for average")
calculate_average(studentId)
generate_top_students_report()
print_students()


# In[ ]:




