import numpy as np

def createMatrix(studentsList):
    matrix = []
    for student in studentsList:
        grades = student.getGrades()
        matrix.append(grades)  
    return np.array(matrix)

def combineMatrices(upperyear, other):
    numStudents = upperyear.shape[0]                                     #get the number of students in the upperyear matrix

    #if a student has not taken a course, then remove it everywhere 
    i = 0
    while i < other.size:
        if other[i] == 0:
            other = np.concatenate((other[0:i], other[i+1:]))
            upperyear = np.concatenate((upperyear[:,:i], upperyear[:,i+1:]), axis = 1)
        else:
            i +=1

    totalStudents = numStudents + 1
    coursestaken = other.size                                      #get the number of courses in the other matrix
    
    newMatrix = np.zeros((totalStudents, coursestaken))
    
    newMatrix[0:numStudents,:] = upperyear[:,0:coursestaken]
    newMatrix[numStudents:, :] = np.array(other)

    return newMatrix

