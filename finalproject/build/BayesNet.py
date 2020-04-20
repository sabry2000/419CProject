#import required packages
import math
from pomegranate import *

def generateBayesianNetwork(course_grade, major_average, major_interest, course_num = "y", student_name = "x"):
    
    #get the course grade
    grade = course_grade/100.0

    #get the major average
    majorAvg = major_average/100.0

    #get the interest level
    interest_level = major_interest/5

    #define the prior distribution cpts
    final_grade = DiscreteDistribution({'Pass': grade, 'Fail': 1-grade})
    enjoyability = DiscreteDistribution({'Fun': interest_level, 'Not Fun': 1-interest_level})

    experience = ConditionalProbabilityTable([
        ['Pass', 'Fun', 'Experienced', 0.90],
        ['Pass', 'Fun', 'Not Experienced', 0.10],
        ['Pass', 'Not Fun', 'Experienced', 0.70],
        ['Pass', 'Not Fun', 'Not Experienced', 0.30],
        ['Fail', 'Fun', 'Experienced', 0.40],
        ['Fail', 'Fun', 'Not Experienced', 0.60],
        ['Fail', 'Not Fun', 'Experienced', 0.10],
        ['Fail', 'Not Fun', 'Not Experienced', 0.90],
    ], [final_grade, enjoyability])

    predicted_course_grade = ConditionalProbabilityTable([
        ['Pass', 'Pass Course', grade],
        ['Pass', 'Fail Course', (1-grade)],
        ['Fail', 'Pass Course', grade - 0.1],
        ['Fail', 'Fail Course', 1-( grade - 0.1)],
    ], [final_grade])

    numberOfMajorCourses = ConditionalProbabilityTable([
        ['Experienced', 0, 0.05],
        ['Experienced', 1, 0.30],
        ['Experienced', 2, 0.65],
        ['Not Experienced', 0, 0.7],
        ['Not Experienced', 1, 0.2],
        ['Not Experienced', 2, 0.1],
    ], [experience])

    majorAverage = ConditionalProbabilityTable([
        ['Experienced', 'Pass Major', majorAvg],
        ['Experienced', 'Fail Major', 1- majorAvg],
        ['Not Experienced', 'Pass Major', majorAvg * 0.8],
        ['Not Experienced', 'Fail Major', 1-(majorAvg - 0.8)]
    ], [experience])

    interests = ConditionalProbabilityTable([
        ['Fun', 'Interested', interest_level],
        ['Fun', 'Not Interested', 1-interest_level],
        ['Not Fun', 'Interested', interest_level*0.8],
        ['Not Fun', 'Not Interested', 1-(interest_level*0.8)]
    ],[enjoyability])

    #define states
    s1 = State( final_grade, name = "Final Grade")
    s2 = State( enjoyability, name = "Enjoyability")
    s3 = State( experience, name = "Experience")
    s4 = State( predicted_course_grade, name = "Predicted Course Grade")
    s5 = State( numberOfMajorCourses, name = "Number Of Major Courses")
    s6 = State( majorAverage, name = "Major Average")
    s7 = State( interests, name = "Interests")

    #Building the Bayesian Network
    network = BayesianNetwork("Creating a Bayesian Network for Student %s for Course %s" % (student_name, course_num))
    network.add_states(s1, s2, s3, s4, s5, s6, s7)
    network.add_edge(s1,s4)
    network.add_edge(s1,s3)
    network.add_edge(s2,s3)
    network.add_edge(s3,s5)
    network.add_edge(s3,s6)
    network.add_edge(s2,s7)
    network.bake()

    return network