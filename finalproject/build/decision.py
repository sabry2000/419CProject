import BayesNetAnalysis
import expectedutility
import config

def getFinalDecisions(finalgrade_probabilities, enjoyability_probabilities):
    final_decisions = []
    eus = []

    for i in range(len(config.upperyearcourses)):
        expected_utilities, total_utility = expectedutility.generateDecisionTree(finalgrade_probabilities[i], enjoyability_probabilities[i])
        if total_utility > config.do_not_take_course:
            final_decisions.append(1)
        else:
            final_decisions.append(0)
        eus.append(expected_utilities)
    
    return final_decisions