#A file containing all of our global variables
import extract
import matrix

#all of the courses that we are studying in this specified order
loweryearcourses = ['COSC 111','COSC 121','MATH 100','MATH 101','PHYS 111','PHYS 121','BIOL 116','BIOL 125','CHEM 111', 'CHEM 121']
upperyearcourses = ['COSC 222','MATH 200', 'PHYS 216', 'BIOL 200', 'CHEM 201']
allcourses = loweryearcourses + upperyearcourses

majors = ['COSC','MATH','PHYS', 'BIOL', 'CHEM']

#extract the students from the csv file
lower_year_students = extract.lower_year
upper_year_students = extract.upper_year

#create the grade matrices of the students
loweryeargrades = matrix.createMatrix(lower_year_students)
upperyeargrades = matrix.createMatrix(upper_year_students)