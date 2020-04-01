import matrix
import numpy as np
from numpy.linalg import norm

def getCosineSimilarity(gradesMatrix):
    numofstudents = gradesMatrix.shape[0]
    # initializing cosine similarity matrix
    cos = np.zeros((numofstudents, numofstudents))
    for i in range(numofstudents):
        for j in range(numofstudents):
            # just set to 1 if it's on the diagonal of cos matrix
            if i is j:
                cos[i][j] = 1
            else:
                # create array with only the 2 students
                comparison = np.array((gradesMatrix[i],gradesMatrix[j]))
                
                # removing this line so we can get a more accurate similarity measure
                # remove a course if 1 of the students hasn't taken it
                comparison = comparison[:, np.all(comparison != 0, axis=0)]
                
                # get similarity of student i and j
                cos[i][j] = np.dot(comparison[0],comparison[1]) / (norm(comparison[0]) * norm(comparison[1]))
    
    return cos

