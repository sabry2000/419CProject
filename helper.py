#helper method that computes the summation part of the collaborative filtering formula, this only includes the controlled students
def computeSum(studentWeights, otherstudentscores, controlledAverages):
    sum = 0
    for i,average in enumerate(controlledAverages):
        sum += studentWeights[i] * (otherstudentscores[i] - average)
    return sum