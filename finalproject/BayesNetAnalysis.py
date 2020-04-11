import config
import BayesNet
import predict
import helper

def performAnalysis(student):
    grades = student.getGrades()
    missingGrades = predict.predictMissingGrades(grades)
    numberofcourses = helper.getNumberOfCourses(grades)
    majorAverages = helper.getMajorsAverages(grades)

    print(grades)
    print(missingGrades)
    print(numberofcourses)
    print(majorAverages)

    for i,major in enumerate(config.majors):
        grade = list(missingGrades[i])[1]
        bn = BayesNet.generateBayesianNetwork(grade, majorAverages[i], int(student.interests[i]), 'x', config.upperyearcourses[i])
        finalcoursegradeprediction = bn.predict_proba({'Predicted Course Grade': 'pass class',
        'Number Of Major Courses': str(numberofcourses[i]),
        'Major Average': 'pass major',
        'Interests': 'Interested'})
        print(finalcoursegradeprediction)

performAnalysis(config.lower_year_students[0])