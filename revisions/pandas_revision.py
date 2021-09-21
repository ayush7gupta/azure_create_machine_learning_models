import pandas as pd
import numpy as np
import wget

study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

marks = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
student_data = np.array([study_hours, marks])
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie',
                                     'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                     'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                            'StudyHours':student_data[0],
                            'Grade':student_data[1]})

print(df_students)

print(df_students.loc[5])

print(df_students.loc[0:5])

print(df_students.iloc[0:5])

print(df_students.iloc[0,[1,2]])

print(df_students.loc[0,'Grade'])

print(df_students.loc[df_students['Name']=='Aisha'])

print(df_students[df_students['Name']=='Aisha'])

print(df_students.query('Name=="Rosie"'))

print(df_students[df_students.Name == 'Aisha'])

url = "https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/ml-basics/grades.csv"
#filename = wget.download(url)
df_students = pd.read_csv('grades.csv', delimiter=',', header='infer')
print(df_students.head())

print(df_students.isnull())

print(df_students.isnull().sum())

print(df_students[df_students.isnull().any(axis=1)])

# filling the NaN values
df_students.StudyHours = df_students.StudyHours.fillna(df_students.StudyHours.mean())
print(df_students)

# remove Na values
df_students = df_students.dropna(axis=0, how='any')
print(df_students)

# Get the mean study hours using to column name as an index
mean_study = df_students['StudyHours'].mean()

# Get the mean grade using the column name as a property (just to make the point!)
mean_grade = df_students.Grade.mean()

# Print the mean study hours and mean grade
print('Average weekly study hours: {:.2f}\nAverage grade: {:.2f}'.format(mean_study, mean_grade))

# Get students who studied for the mean or more hours
print(df_students[df_students.StudyHours > mean_study])

print(df_students[df_students.StudyHours > mean_study].Grade.mean())

passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)

print(df_students)

print(df_students.groupby(df_students.Pass).Name.count())

print(df_students.groupby(df_students.Pass)['StudyHours', 'Grade'].mean())

# Create a DataFrame with the data sorted by Grade (descending)
df_students = df_students.sort_values('Grade', ascending=False)

# Show the DataFrame
print(df_students)
