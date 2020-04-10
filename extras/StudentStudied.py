from config import *

class StudentStudied:
    courseGrades = []
    coursesTaken = []
    missingCourses = []

    #student constructor
    def __init__(self, courseGrades, majorInterests):
        self.analyzeCourseGrades(courseGrades)
        self.majorInterests = majorInterests
    
    def analyzeCourseGrades(self, courseGrades):
        for courseGrade in courseGrades:
            if courseGrade[1] != '0':
                self.coursesTaken.append(courseGrade[0])
                self.courseGrades.append(courseGrade)
            else:
                self.missingCourses.append(courseGrade[0])
    
    #function to add a course grade tuple to the student
    def addCourseGrade(self, course_code, grade):
        courseGrade = (course_code, grade)
        self.courseGrades.append(courseGrade)
        self.coursesTaken.append(course_code)
        self.missingCourses.pop(course_code)
