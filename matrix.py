import numpy as np

def createMatrix(data, isStudent):
    matrix = []
    if not isStudent:
        for student in data:
            grades = student.getGrades()
            matrix.append(grades)
        matrix = np.array(matrix)    
    else:
        matrix = np.asmatrix(data)
    return matrix

def combineMatrices(matrix1, matrix2):
    numStudents1 = matrix1.shape[0]                                     #get the number of students in the first matrix
    numStudents2 = matrix2.shape[0]                                     #get the number of students in the second matrix
    numCourses1 = matrix1.shape[1]                                      #get the number of courses in the first matrix
    numCourses2 = matrix2.shape[1]                                      #get the number of courses in the second matrix


    totalStudents = numStudents1 + numStudents2
    
    if numCourses1 > numCourses2:
        biggerMatrix = matrix1
        smallerMatrix = matrix2
    else:
        biggerMatrix = matrix2
        smallerMatrix = matrix1

    bigmatrixstudents = biggerMatrix.shape[0]
    maxCourses = biggerMatrix.shape[1]
    
    newMatrix = np.zeros((totalStudents, maxCourses))
 
    newMatrix[0:bigmatrixstudents,0:] = biggerMatrix
    newMatrix[bigmatrixstudents:, 0 : smallerMatrix.shape[1]] = smallerMatrix

    return newMatrix

def getMeans(matrix):
    #get the count of non-zeros in each row and use that for averaging the summation along each row
    averages = np.true_divide(matrix.sum(1),(matrix!=0).sum(1))

    return averages
