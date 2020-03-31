import csv
import numpy as np
from numpy.linalg import norm
import config
import ControlledStudent as cs

def predictGrades():
    grades = []

    #appending our controlled students to our numpy array
    for student in config.controlledStudents:
        studentgrades = student.getGrades()
        print(studentgrades)
        grades.append(studentgrades)

    #appending the experimental student grades to our numpy array
    for student in config.experimentalStudents:
        studentgrades = student.firstyearcourses
        print(studentgrades)
        grades.append(studentgrades)

    # turning data into a numpy array
    grades = np.array(([i for i in grades]), dtype=float)

    numStudents = grades.shape[0]

# initializing cosine similarity matrix
cos = [[0 for i in range(numStudents)] for j in range(numStudents)]
for i in range(numStudents):
    for j in range(numStudents):
        # just set to 1 if it's on the diagonal of cos matrix
        if i is j:
            cos[i][j] = 1
        else:
            # create array with only the 2 students
            comparison = np.array((grades[i],grades[j]))
            # removing this line so we can get a more accurate similarity measure
                # remove a course if 1 of the students hasn't taken it
                # comparison = comparison[:, np.all(comparison != 0, axis=0)]
            # get similarity of student i and j
            cos[i][j] = np.dot(comparison[0],comparison[1]) / (norm(comparison[0]) * norm(comparison[1]))

for i in cos:
    print(i)

sims = int(input("How many similar people do you want to include? (Up to %i) " % (numStudents-1)))
stu = int(input("Who do you want to look at? "))
mark = int(input("What class mark do you want to predict? "))

# get 'stu' most similar students (ignoring themselves)
homies = dict(zip([i for i in range(numStudents)],cos[stu]))
homies = list({k: v for k, v in sorted(homies.items(), key=lambda item: item[1], reverse=True)}.keys())[1:sims+1]

# initialize estimate with mean of user
predGrade = np.mean(grades[stu][grades[stu] != 0])

# add what is essentially the MSE of each similar student for that given class
for i in homies:
    predGrade += (grades[i][mark]-np.mean(grades[i][grades[i] !=0])) / len(homies)

# here you go!
print(predGrade)

# part of above code to test prediction with cosine function in cos_sim
def GradeFromCos(cosSim,numSim,student,lecture):
    
    homies = dict(zip([i for i in range(numStudents)],cos[stu]))
    ranks = list({k: v for k, v in sorted(homies.items(), key=lambda item: item[1], reverse=True)}.keys())[1:sims+1]
    summation = sum(list({k: v for k, v in sorted(homies.items(), key=lambda item: item[1], reverse=True)}.values())[1:sims+1])

    predGrade = np.mean(grades[student][grades[student] != 0])

    for i in ranks:
        predGrade += (grades[i][lecture] - np.mean(grades[i][grades[i] !=0])) * (homies.get(i)/summation)
    
    return predGrade