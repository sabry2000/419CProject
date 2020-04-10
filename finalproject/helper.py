#This file contains helper methods
import numpy as np

#helper method that computes the summation part of the collaborative filtering formula, this only includes the controlled students
def computeSum(studentWeights, otherstudentscores, controlledAverages):
    sum = 0
    for i,average in enumerate(controlledAverages):
        sum += studentWeights[i] * (otherstudentscores[i] - average)
    return sum

def getMeans(matrix):
    #get the count of non-zeros in each row and use that for averaging the summation along each row
    averages = np.true_divide(matrix.sum(1),(matrix!=0).sum(1))

    return averages