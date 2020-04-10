#import required packages
import math
from pomegranate import *

def generateBayesianNetwork(course_grade, major_average, major_interest):
    
    #get the course grade
    grade = course_grade/100.0

    #get the major average
    majorAvg = major_average/100.0

    #get the interest level
    interest_level = major_interest/5

    #define the prior distribution cpts
    predicted_course_grade = DiscreteDistribution({ 'pass class': grade, 'fail class': 1 - grade })         #P = 'Pass, F = 'Fail'
    numberOfMajorCourses = DiscreteDistribution({'0': 1./3, '1': 1./3, '2': 1./3})
    majorAverage = DiscreteDistribution({'pass major': majorAvg, 'fail major': 1- majorAvg})                #P = 'Pass, F = 'Fail'
    interests = DiscreteDistribution({'Interested': interest_level, 'Not Interested': 1-interest_level})    #I = 'Interested', NI = 'Not Interested'

    #define experience as the intermediate cpt
    experience = ConditionalProbabilityTable([
        ['Experienced','0', 'pass major', 0.90],
        ['Experienced','0', 'fail major', 0.90],
        ['Experienced','1', 'pass major', 0.90],
        ['Experienced','1', 'fail major', 0.90],
        ['Experienced','2', 'pass major', 0.90],
        ['Experienced','2', 'fail major', 0.90],
        ['Not Experienced','0', 'pass major', 0.90],
        ['Not Experienced','0', 'fail major', 0.90],
        ['Not Experienced','1', 'pass major', 0.90],
        ['Not Experienced','1', 'fail major', 0.90],
        ['Not Experienced','2', 'pass major', 0.90],
        ['Not Experienced','2', 'fail major', 0.90]
    ], [numberOfMajorCourses, majorAverage])

    #define the final cpts
    finalGrade = ConditionalProbabilityTable([
        ['Pass','pass class', 'Experienced', 0.90],
        ['Pass','pass class', 'Not Experienced', 0.90],
        ['Pass','fail class', 'Experienced', 0.90],
        ['Pass','fail class', 'Not Experienced', 0.90],
        ['Fail','pass class', 'Experienced', 0.90],
        ['Fail','pass class', 'Not Experienced', 0.90],
        ['Fail','fail class', 'Experienced', 0.90],
        ['Fail','fail class', 'Not Experienced', 0.90],

    ], [predicted_course_grade, experience])

    enjoyability = ConditionalProbabilityTable([
        ['fun','Interested', 'Experienced', 0.90],
        ['fun','Interested', 'Not Experienced', 0.90],
        ['fun','Not Interested', 'Experienced', 0.90],
        ['fun','Not Interested', 'Not Experienced', 0.90],
        ['not fun','Interested', 'Experienced', 0.90],
        ['not fun','Interested', 'Not Experienced', 0.90],
        ['not fun','Not Interested', 'Experienced', 0.90],
        ['not fun','Not Interested', 'Not Experienced', 0.90],
    ], [interests, experience])

    #define states
    s1 = State( predicted_course_grade, name = "Predicted Course Grade")
    s2 = State( numberOfMajorCourses, name = "Number Of Major Courses")
    s3 = State( majorAverage, name = "Major Average")
    s4 = State( interests, name = "Interests")
    s5 = State( experience, name = "Experience")
    s6 = State( finalGrade, name = "Final Grade")
    s7 = State( enjoyability, name = "Enjoyability")

    #Building the Bayesian Network
    network = BayesianNetwork("Creating a Bayesian Network for Student %s for Course %s", x, y)
    network.add_states(s1, s2, s3, s4, s5, s6, s7)
    network.add_edge(s2,s5)
    network.add_edge(s3,s5)
    network.add_edge(s1,s6)
    network.add_edge(s5,s6)
    network.add_edge(s4,s7)
    network.add_edge(s5,s7)
    network.bake()

    return network