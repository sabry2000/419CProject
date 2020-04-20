#A file containing all of our global variables
import extract
import matrix

#all of the courses that we are studying in this specified order
loweryearcourses = ['COSC 111','COSC 121','MATH 100','MATH 101','PHYS 111','PHYS 121','BIOL 116','BIOL 125','CHEM 111', 'CHEM 121']
upperyearcourses = ['COSC 222','MATH 200', 'PHYS 216', 'BIOL 200', 'CHEM 201']
allcourses = loweryearcourses + upperyearcourses

#all the majors that we are studying
majors = ['COSC','MATH','PHYS', 'BIOL', 'CHEM']

#the possible decisions and their utilities
enjoy_and_do_well = 10
enjoy_and_do_bad = 0
dislike_and_do_well = 0
dislike_and_do_bad = -10
do_not_take_course = 5

#The different lotteries
lottery1 = [enjoy_and_do_well, enjoy_and_do_bad, dislike_and_do_well, dislike_and_do_bad]
lottery2 = [do_not_take_course]

#extract the students from the csv file
lower_year_students = extract.lower_year
upper_year_students = extract.upper_year

#create the grade matrices of the students
loweryeargrades = matrix.createMatrix(lower_year_students)
upperyeargrades = matrix.createMatrix(upper_year_students)

#extract the averages of all the students
upperyearaverages = [student.average for student in upper_year_students]
loweryearaverages = [student.average for student in lower_year_students]   