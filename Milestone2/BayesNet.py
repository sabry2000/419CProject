#import required packages
import math
from pomegranate import *

#get the course grade
grade = get_course_grade()/100.0

#get the major average
majorAvg = get_major_average()/100.0

#get the interest level
interest_level = get_interest_level()/100.0

#define the prior distribution cpts
predicted_course_grade = DiscreteDistribution({ 'P': grade, 'F': 1 - grade })                       #P = 'Pass, F = 'Fail'
numberOfMajorCourses = DiscreteDistribution({'1': 1./4, '2': 1./4, '3': 1./4, '4': 1./4})
majorAverage = DiscreteDistribution({'P': majorAvg, 'F': 1- majorAvg})                              #P = 'Pass, F = 'Fail'
interests = DiscreteDistribution({'I': interest_level, 'NI': 1-interest_level})                     #I = 'Interested', NI = 'Not Interested'

#define the intermediate cpts
experience = ConditionalProbabilityTable([

], [numberOfMajorCourses, majorAverage])

finalGrade = ConditionalProbabilityTable([

], [predicted_course_grade, experience])

fun = ConditionalProbabilityTable([

], [experience, interests])

#define states
s1 = State( predicted_course_grade, name = "Predicted Course Grade")
s2 = State( numberOfMajorCourses, name = "Number Of Major Courses")
s3 = State( majorAverage, name = "Major Average")
s4 = State( interests, name = "Average")
s5 = State( experience, name = "Experience")
s6 = State( finalGrade, name = "Final Grade")
s7 = State( fun, name = "Fun")

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
