import extract as e

#all of the courses that we are studying in this specified order
loweryearcourses = ['COSC 111','COSC 121','MATH 100','MATH 101','PHYS 111','PHYS 121','BIOL 116','BIOL 125','CHEM 111', 'CHEM 121']
upperyearcourses = ['COSC222','MATH200','PHYS216', 'BIOL 200', 'CHEM 201']
allcourses = loweryearcourses + upperyearcourses

majors = ['COSC','MATH','PHYS', 'BIOL', 'CHEM']

#initialize arrays to hold different types of students
controlled = e.controlled
experimental = e.experimental
