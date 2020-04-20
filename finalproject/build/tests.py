import Student

#Realistic
#student who doesn't know anything
def testCase1():
    x = Student.LYStudent([0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0])
    return x

#student who knows everything
def testCase2():
    x = Student.LYStudent([100,100,100,100,100,100,100,100,100,100], [5,5,5,5,5])
    return x

#Unrealistic
#over achiever
def testCase3():
    x = Student.LYStudent([120,204,123,234,56,707,456,775,567,345], [6,6,6,6,6])
    return x

#under achiever
def testCase4():
    x = Student.LYStudent([-123,-34,3,24,56,77,-6,-5,-7,-5], [-1,2,5,-2,-5])
    return x