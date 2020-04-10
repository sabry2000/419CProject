import matrix
import helper
import array
import config

import numpy as np

from cos_sim import getCosineSimilarity as getCS

def predictMissingGrades(studentGrades):
    
    #get the grades of the student and convert into a matrix
    gradesMatrix = np.asmatrix(studentGrades)

    #combine matrices and get the similarity matrices
    grades = matrix.combineMatrices(config.upperyeargrades,gradesMatrix)
    weights = getCS(grades)

    #get the averages of both student types
    allAverages = helper.getMeans(grades)
    studentAverage = allAverages[allAverages.shape[0] - 1]
    upperyearaverages = allAverages[0:allAverages.shape[0] - 1]

    #get the indices of the missing grades, i.e. where the '0's are
    studentStudied = grades.shape[0]
    
    #the weights of all the students relative to the student being studied
    studentWeights = weights[studentStudied-1]

    missingGrades = []

    for i,course in enumerate(grades[studentStudied-1]):
        #if it is a missing course predict its grade
        if course == 0:
            otherstudentscores = np.array([score for score in config.upperyeargrades[:,i] ])
            finalcoursegrade = studentAverage + helper.computeSum(studentWeights, otherstudentscores, upperyearaverages)
            grade = array.array('f', np.ravel(np.asarray(finalcoursegrade)))
            grade = grade[0]
            element = tuple((config.allcourses[i], grade))
            missingGrades.append(element)
    
    missingUpperYearCourses = []
    for i,grade in enumerate(missingGrades):
        course = list(grade)[0]
        if course in config.upperyearcourses:
            missingUpperYearCourses.append(grade)
    
    return missingUpperYearCourses