import config
import BayesNet
import predict
import helper

def performAnalysis(student):
    grades = student.getGrades()
    missingGrades = predict.predictMissingGrades(grades)
    numberofcourses = helper.getNumberOfCourses(grades)
    majorAverages = helper.getMajorsAverages(grades)

    for i,major in enumerate(config.majors):
        bn = BayesNet.generateBayesianNetwork(missingGrades[i], majorAverages[i], student.interests[i], 'x', config.upperyearcourses[i])
        finalcoursegradeprediction = bn.predict_proba({'Predicted Course Grade': 'pass class',
        'Number Of Major Courses': str(numberofcourses[i]),
        'Major Average': 'pass major',
        'Interests': 'Interested'})

