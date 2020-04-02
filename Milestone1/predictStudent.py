from matrix import *
from helper import computeSum
from cos_sim import getCosineSimilarity as getCS
import config
import array

def predictStudentGrades(controlled, studentGrades):
    
    #get the grades of both student types and convert into a matrix
    controlledGrades = createMatrix(controlled, 0)
    gradesMatrix = createMatrix(studentGrades, 1)

    #combine matrices and get the similarity matrices
    grades = combineMatrices(gradesMatrix, controlledGrades)
    weights = getCS(grades)

    print(grades)

    #get the averages of both student types
    allAverages = getMeans(grades)
    studentAverage = allAverages[allAverages.shape[0] - 1]
    controlledAverages = allAverages[0:allAverages.shape[0] - 1]

    print(studentAverage)
    print(controlledAverages)

    #get the indices of the missing grades, i.e. where the '0's are
    studentStudied = grades.shape[0]
    
    #the weights of all the students relative to the student being studied
    studentWeights = weights[studentStudied-1]

    missingGrades = []

    for i,course in enumerate(grades[studentStudied-1]):
        #if it is a missing course predict its grade
        if course == 0:
            otherstudentscores = np.array([score for score in controlledGrades[:,i] ])
            finalcoursegrade = studentAverage + computeSum(studentWeights, otherstudentscores, controlledAverages)
            grade = array.array('f', np.ravel(np.asarray(finalcoursegrade)))
            grade = grade[0]
            element = tuple((config.allcourses[i], grade))
            missingGrades.append(element)
    
    return missingGrades

student = [90,100]
print(predictStudentGrades(config.controlled, student))
