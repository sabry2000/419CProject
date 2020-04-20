import matrix
import numpy as np
from numpy.linalg import norm
import math

def getCosineSimilarity(gradesMatrix):
    numofstudents = gradesMatrix.shape[0]
    # initializing cosine similarity matrix
    cos = np.zeros(numofstudents)

    studentgrades = gradesMatrix[numofstudents-1]
    for i in range(numofstudents):
        # just set to 1 if it's on the diagonal of cos matrix
        if i is numofstudents-1:
            cos[i] = 1
        else:
            # get similarity of student i and j
            #cos[i] = np.dot(gradesMatrix[i],gradesMatrix[numofstudents-1]) / (norm(babygradesMatrix[i]) * studentMagnitude)
            difference = np.subtract(gradesMatrix[i], studentgrades)
            normalized = [value*2*math.pi/100 for value in difference]
            similarity = [math.cos(math.radians(angle)) for angle in normalized]
            cos[i] = norm(similarity)/norm(studentgrades)
    return cos/norm(cos)

