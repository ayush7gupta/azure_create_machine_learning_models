data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
print(data)

import numpy as np

grades = np.array(data)
print(grades)

print (type(data),'x 2:', data * 2)
print('---')
print (type(grades),'x 2:', grades * 2)

print(grades.shape)
print(grades[0])

print(grades.mean())

study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

student_data = np.array([study_hours, grades])

print(student_data)
print(student_data.shape)

print(student_data[1][0])

avg_marks = student_data[1].mean()
avg_study = student_data[0].mean()

print(avg_marks)
print(avg_study)