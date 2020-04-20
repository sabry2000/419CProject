import numpy as np

def createMatrix(studentsList):
    matrix = []
    for student in studentsList:
        grades = student.getGrades()
        matrix.append(grades)
    
    return np.array(matrix)

def combineMatrices(upperyear, other):
    numStudents1 = upperyear.shape[0]                                     #get the number of students in the upperyear matrix
    numStudents2 = other.shape[0]                                     #get the number of students in the other matrix
    totalcourses = upperyear.shape[1]                                      #get the number of courses in the upperyear matrix
    coursestaken = other.shape[1]                                      #get the number of courses in the other matrix

    totalStudents = numStudents1 + numStudents2
    
    newMatrix = np.zeros((totalStudents, totalcourses))
    
    newMatrix[0:numStudents1,0:] = upperyear
    newMatrix[numStudents1:, 0 : coursestaken] = other

    return newMatrix

