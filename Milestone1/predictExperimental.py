from matrix import *
from cos_sim import getCosineSimilarity as getCS
import numpy as np
import array
import config
from helper import computeSum

#this function predicts the grades of the experimental students in our csv file
def predictExperimentalGrades(controlled, experimental):
    
    #get the grades of both student types and convert into a matrix
    controlledGrades = createMatrix(controlled,False)
    experimentalGrades = createMatrix(experimental,False)

    #get the averages of the both student types
    controlledAverages = controlledGrades.mean(1)

    #combine matrices and get the similarity matrices
    grades = combineMatrices(controlledGrades, experimentalGrades)
    weights = getCS(grades)

    #get all the average grades for all the students
    allAverages = getMeans(grades)

    #get the indices of the missing grades, i.e. where the '0's are
    studentsStart = controlledGrades.shape[0]                              #A grades matrix will look like this:
    coursesStart = experimentalGrades.shape[1]                             #[[x y z w q u i] This top part is the "controlled students
    studentsEnd = grades.shape[0]                                          # [a h e f h w u]
    coursesEnd = controlledGrades.shape[1]                                 # [q u i 0 0 0 0]] This bottom part is the "experimental" students

    allStudentsMissingCourses = []
    for student in range(studentsStart,studentsEnd):

        #the current average of the current student
        currentAverageGrade = allAverages[student]

        #the weights of all the students relative to the student being studied
        studentWeights = weights[student]

        missingGrades = []
        
        for course in range(coursesStart,coursesEnd):
            otherstudentscores = np.array([score for score in controlledGrades[:,course] ])
            finalcoursegrade = currentAverageGrade + computeSum(studentWeights, otherstudentscores, controlledAverages)
            missingGrades.append(finalcoursegrade)
        allStudentsMissingCourses.append(missingGrades)

    return np.asmatrix(allStudentsMissingCourses)

print(predictExperimentalGrades(config.controlled, config.experimental))
