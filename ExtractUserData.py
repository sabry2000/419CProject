from config import *
from StudentStudied import StudentStudied

#function to generate questions that will be asked to the user
def generateQuestions():
    
    #lists to hold course and major questions
    courseQuestions = []
    majorQuestions = []
    
    question_parts = ["? (if not applicable please type 0) ", "How interested are you in ",  "? (1 to 5) "]

    for course in courses:
        courseQuestion = course + question_parts[0] 
        courseQuestions.append(courseQuestion)
    
    for major in majors:
        majorQuestion = question_parts[1] + major + question_parts[2]
        majorQuestions.append(majorQuestion)
    
    return courseQuestions, majorQuestions

def extractUserInfo():
    courseQuestions, majorQuestions = generateQuestions()
    courseGrades = []
    majorInterests = []

    #get the user grades for all of our courses
    for i, question in enumerate(courseQuestions):
        answer = input(question)
        courseGrade = (courses[i], answer)
        courseGrades.append(courseGrade)
    
    #get the interest of the user in our majors
    for i, question in enumerate(majorQuestions):
        answer = input(question)
        majorInterest = (majors[i], answer)
        majorInterests.append(majorInterest)
    
    return StudentStudied(courseGrades,majorInterests)

