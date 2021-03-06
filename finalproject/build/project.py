import predict
import BayesNetAnalysis
import decision
import config

import tests

def runproject(student):

    #predict the missing grades
    predictedGrades = predict.predictMissingGrades(student)
    print(predictedGrades)
    
    #perform the bayes net analysis
    finalgrade_probabilities, enjoyability_probabilities = BayesNetAnalysis.performAnalysis(student, predictedGrades)
    
    #get the final decisions
    decisions = decision.getFinalDecisions(finalgrade_probabilities, enjoyability_probabilities)
    
    #display the results
    for i,course in enumerate(config.upperyearcourses):
        print('This student should %stake %s'% ('' if decisions[i] == 1 else 'not ', course))
        print('Your predicted grade for %s is %f%s and your interest level is %i%s'%(course,finalgrade_probabilities[i]*100, '%',
        enjoyability_probabilities[i]*100, '%'))

def printToGUI(student, courses="all"):

    #predict the missing grades
    predictedGrades = predict.predictMissingGrades(student)
    print(predictedGrades)
    
    #perform the bayes net analysis
    finalgrade_probabilities, enjoyability_probabilities = BayesNetAnalysis.performAnalysis(student, predictedGrades)
    
    #get the final decisions
    decisions = decision.getFinalDecisions(finalgrade_probabilities, enjoyability_probabilities)
    
    prediction = ""
    
    if(courses == "all"):
        #display the results
        for i,course in enumerate(config.upperyearcourses):
            prediction += 'This student should %stake %s\n'% ('' if decisions[i] == 1 else 'not ', course)
            prediction += 'Your predicted grade for %s is %f%s and your interest level is %i%s\n'%(course,finalgrade_probabilities[i]*100, '%',
            enjoyability_probabilities[i]*100, '%')
    
    else:
        for i,course in enumerate(config.upperyearcourses):
            if(course == courses):
                prediction += 'This student should %stake %s\n'% ('' if decisions[i] == 1 else 'not ', course)
                prediction += 'Your predicted grade for %s is %f%s and your interest level is %i%s\n'%(course,finalgrade_probabilities[i]*100, '%',
                enjoyability_probabilities[i]*100, '%')

    return prediction


if __name__ == "__main__":
    #for i,student in enumerate(config.lower_year_students):
    #    print("Student %i" % i)
    #    runproject(student)
    #    print("\n\n")
    runproject(config.lower_year_students[0])
    #runproject(tests.testCase4())