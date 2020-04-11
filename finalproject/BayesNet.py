#import required packages
import math
from pomegranate import *

def generateBayesianNetwork(course_grade, major_average, major_interest, student_name, course_num):
    
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

    experience = ConditionalProbabilityTable([
    ['0', 'pass major','Experienced', 0.70],
    ['0', 'pass major','Not Experienced', 0.30],
    ['0', 'fail major','Experienced', 0.60],
    ['0', 'fail major','Not Experienced', 0.40],
    ['1', 'pass major','Experienced', 0.80],
    ['1', 'pass major','Not Experienced', 0.20],
    ['1', 'fail major','Experienced', 0.40],
    ['1', 'fail major','Not Experienced', 0.60],
    ['2', 'pass major','Experienced', 0.90],
    ['2', 'pass major','Not Experienced', 0.10],
    ['2', 'fail major','Experienced', 0.50],
    ['2', 'fail major','Not Experienced', 0.50]
    ], [numberOfMajorCourses, majorAverage])

    #define the final cpts
    finalGrade = ConditionalProbabilityTable([
    ['pass class', 'Experienced', 'Pass', 0.95],
    ['pass class', 'Experienced', 'Fail', 0.05],
    ['pass class', 'Not Experienced', 'Pass', 0.75],
    ['pass class', 'Not Experienced', 'Fail', 0.25],
    ['fail class', 'Experienced', 'Pass', 0.60],
    ['fail class', 'Experienced', 'Fail', 0.40],
    ['fail class', 'Not Experienced', 'Pass', 0.40],
    ['fail class', 'Not Experienced', 'Fail', 0.60]
    ], [predicted_course_grade, experience])

    enjoyability = ConditionalProbabilityTable([
    ['Interested', 'Experienced', 'fun', 0.90],
    ['Interested', 'Experienced', 'not fun', 0.10],
    ['Interested', 'Not Experienced', 'fun', 0.75],
    ['Interested', 'Not Experienced', 'not fun', 0.25],
    ['Not Interested', 'Experienced', 'fun', 0.60],
    ['Not Interested', 'Experienced', 'not fun', 0.40],
    ['Not Interested', 'Not Experienced', 'fun', 0.40],
    ['Not Interested', 'Not Experienced', 'not fun', 0.60]
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
    network = BayesianNetwork("Creating a Bayesian Network for Student %s for Course %s" % (student_name, course_num))
    network.add_states(s1, s2, s3, s4, s5, s6, s7)
    network.add_edge(s2,s5)
    network.add_edge(s3,s5)
    network.add_edge(s1,s6)
    network.add_edge(s5,s6)
    network.add_edge(s4,s7)
    network.add_edge(s5,s7)
    network.bake()

    return network

#print(generateBayesianNetwork(90,90,3, 'ahmed', 'cosc 222'))