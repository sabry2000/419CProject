class ControlledStudent:

    major = ''
    cosc111 = 0
    cosc121 = 0
    cosc222 = 0
    math100 = 0
    math101 = 0
    math200 = 0
    phys111 = 0
    phys121 = 0
    phys216 = 0
    biol116 = 0
    biol125 = 0
    biol200 = 0
    chem111 = 0
    chem121 = 0
    chem201 = 0
    loweryearcourses = []
    upperyearcourses = []
    
    def __init__(self, loweryearcourses,upperyearcourses,major):
        
        cosc111 = loweryearcourses[0]
        cosc121 = loweryearcourses[1]
        math100 = loweryearcourses[2]
        math101 = loweryearcourses[3]
        phys111 = loweryearcourses[4]
        phys121 = loweryearcourses[5]
        biol116 = loweryearcourses[6]
        biol125 = loweryearcourses[7]
        chem111 = loweryearcourses[8]
        chem121 = loweryearcourses[9]
        cosc222 = upperyearcourses[0]
        math200 = upperyearcourses[1]
        phys216 = upperyearcourses[2]
        biol200 = upperyearcourses[3]
        chem201 = upperyearcourses[4]

        self.major = major
        self.cosc111 = cosc111
        self.cosc121 = cosc121
        self.cosc222 = cosc222
        self.math100 = math100
        self.math101 = math101
        self.math200 = math200
        self.phys111 = phys111
        self.phys121 = phys121
        self.phys216 = phys216
        self.biol116 = biol116
        self.biol125 = biol125
        self.biol200 = biol200
        self.chem111 = chem111
        self.chem121 = chem121
        self.chem201 = chem201
        self.loweryearcourses = loweryearcourses
        self.upperyearcourses = upperyearcourses
    
    def getGrades(self):
        return self.loweryearcourses + self.upperyearcourses
