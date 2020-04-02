from extract import controlled, experimental
from config import *
from predictExperimental import predictExperimentalGrades
from predictStudent import predictStudentGrades
import QueryGUI as gui

while True:
    userAction = gui.getUserInput()
    if userAction == 'Display Predicted Experimental Grades':
        gui.display(predictExperimentalGrades)
    elif userAction == 'Display Course Grade':
        predictedStudentGrades = predictStudentGrades()
        coursename = gui.getCourseName()
        grade = getCourseGrade(predictStudentGrades, coursename)
        gui.display(grade)