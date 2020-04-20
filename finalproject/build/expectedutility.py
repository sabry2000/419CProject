import config

def generateDecisionTree(finalgrade_probability, enjoyability_probability):
    #get the probabilities of each decision
    prob1 = finalgrade_probability * enjoyability_probability
    prob2 = (1-finalgrade_probability) * enjoyability_probability
    prob3 = finalgrade_probability * (1-enjoyability_probability)
    prob4 = (1-finalgrade_probability) * (1-enjoyability_probability)

    probabilities = [prob1, prob2, prob3, prob4]

    expected_utilities = []
    total_utility = 0
    
    #get the eu of each decision and store it
    for i,decision in enumerate(config.lottery1):
        expected_utility = getExpectedUtility(decision, probabilities[i])
        total_utility += expected_utility
        expected_utilities.append(expected_utility)
    
    return expected_utilities, total_utility

def getExpectedUtility(utility, probability):
    return utility * probability