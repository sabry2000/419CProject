import matrix
import array
import config
import cos_sim
import numpy as np

def predictMissingGrades(student):

    #get the grades of the student
    studentGrades = student.getGrades()
    
    #get the grades of the student and convert into a matrix
    gradesMatrix = np.array(studentGrades)

    #combine matrices and get the similarity matrices
    grades = matrix.combineMatrices(config.upperyeargrades,gradesMatrix)
    weights = cos_sim.getCosineSimilarity(grades)

    #get the student's average
    studentmajoraverages = student.majorAverages

    missingGrades = []

    for i in range(len(config.upperyearcourses)):
        otherstudentscores = [score for score in config.upperyeargrades[:,(i + len(config.loweryearcourses))]]
        
        #Computes the summation part of the collaborative filtering formula
        summation = 0.0
        
        for j,average in enumerate(config.upperyearaverages):
            summation = summation + weights[j] * (otherstudentscores[j] - average)
        
        coursegrade = studentmajoraverages[i] + summation
        missingGrades.append(coursegrade)
    
    return missingGrades