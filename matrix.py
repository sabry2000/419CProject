import numpy as np

def createMatrix(data, isStudent):
    allGrades = []

    if ~isStudent:
        for student in data:
            grades = student.getGrades()
            allGrades.append(grades)
        matrix = np.array(allGrades)    
    else:
        for course in data.coursesTaken:
            grade = course[1]
            allGrades.append(grade)       
        matrix = np.array(data.allGrades)

    return matrix

def combineMatrices(matrix1, matrix2):
    numStudents1 = matrix1.shape[0]                                      #get the number of students in the first matrix
    numCourses1 = matrix1.shape[1]                                      #get the number of courses in the first matrix
    numStudents2 = matrix2.shape[0]                                     #get the number of students in the second matrix
    numCourses2 = matrix2.shape[1]                                      #get the number of courses in the second matrix

    totalStudents = numStudents1 + numStudents2
    minStudents = min(numStudents1, numStudents2)
    maxCourses = max(numCourses1, numCourses2)
    minCourses = min(numCourses1, numCourses2)
    
    biggerMatrix = (matrix1) if maxCourses == numCourses1 else matrix2
    smallerMatrix = (matrix1) if minCourses == numCourses1 else matrix2

    x = biggerMatrix.shape[0]

    newMatrix = np.zeros((totalStudents, maxCourses))
    remaining = np.zeros((minStudents, maxCourses - minCourses))

    newMatrix[0:x,0:] = biggerMatrix
    newMatrix[x:, 0 : minCourses] = smallerMatrix
    newMatrix[x: totalStudents, minCourses:maxCourses] = remaining

    return newMatrix
