#import predict

class UYStudent:
    
    def __init__(self, loweryearcourses,upperyearcourses,major):
        
        self.major = major
        self.loweryearcourses = loweryearcourses
        self.upperyearcourses = upperyearcourses
        self.allCourses = self.loweryearcourses + upperyearcourses
        self.numberOfCourses = self.getNumOfCourses()
        self.average = self.getAverage()
    
    def getNumOfCourses(self):
        tot = 0
        for course in self.allCourses:
            tot += 1 if course !=0 else 0
        return tot
    
    def getGrades(self):
        return self.allCourses
    
    def getAverage(self):
        average = 0
        if self.numberOfCourses != 0:
            for course in self.allCourses:
                if course < 0 or course > 100:
                    raise Exception("Check Database")
            average = sum(self.allCourses)/self.numberOfCourses
        return average

class LYStudent:

    def __init__(self, loweryearcourses, interests):
        self.loweryearcourses = loweryearcourses
        self.interests = interests
        self.numberOfCourses = self.getNumOfCourses()
        self.average = self.getAverage()
        self.majorAverages = self.getMajorAverages()
    
    def getNumOfCourses(self):
        numbers = [0, 0, 0, 0, 0]
        for i,course in enumerate(self.loweryearcourses):
            if course != 0:
                numbers[int(i/2)] = numbers[int(i/2)] + 1
        return numbers
    
    def getGrades(self):
        return self.loweryearcourses
    
    def getMajorAverages(self):
        averages = []
        for i in range(int(len(self.loweryearcourses)/2)):
            course1 = self.loweryearcourses[2*i]
            course2 = self.loweryearcourses[2*i + 1]
            averages.append((course1 + course2) / 2.0  )
        return averages

    def getAverage(self):
        average = 0
        if sum(self.numberOfCourses) != 0:
            for lyc in self.loweryearcourses:
                if lyc < 0 or lyc > 100:
                    raise Exception("Incorrect input")
            average = sum(self.loweryearcourses)/sum(self.numberOfCourses)
        return average
                
