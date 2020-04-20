import config
import BayesNet
import predict

def performAnalysis(student, predictedGrades):
    numberofcourses = student.numberOfCourses
    majorAverages = student.majorAverages
    interests = student.interests

    finalgrade_probabilities = []
    enjoyability_probabilities = []
    for i,course in enumerate(config.upperyearcourses):
        grade = predictedGrades[i]
        numofcourses = numberofcourses[i]
        majorAverage = majorAverages[i]
        interest = interests[i]

        #generate the bayes net
        bn = BayesNet.generateBayesianNetwork(grade, majorAverage, interest, course)
        
        #perform inference
        predictions = bn.predict_proba({
            'Predicted Course Grade': 'Pass Course',
            'Number Of Major Courses': numofcourses,
            'Major Average': 'Pass Major',
            'Interest': 'Interested'
        }, 1)

        #extract probabilities
        finalgrade_probability = predictions[0].parameters
        finalgrade_probability = finalgrade_probability[0]['Pass']
        enjoyability_probability = predictions[1].parameters
        enjoyability_probability = enjoyability_probability[0]['Fun']

        #store probabilities
        finalgrade_probabilities.append(finalgrade_probability)
        enjoyability_probabilities.append(enjoyability_probability)
        
    return finalgrade_probabilities, enjoyability_probabilities