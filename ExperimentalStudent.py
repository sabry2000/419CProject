class ExperimentalStudent:

    major = ''
    cosc111 = 0
    cosc121 = 0
    math100 = 0
    math101 = 0
    phys111 = 0
    phys121 = 0
    biol116 = 0
    biol125 = 0
    chem111 = 0
    chem121 = 0
    COSCinterest = 0
    MATHinterest = 0
    PHYSinterest = 0
    BIOLinterest = 0
    CHEMinterest = 0
    loweryearcourses = []
    interests = []

    def __init__(self, loweryearcourses, interests):
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
        COSCinterest = interests[0]
        MATHinterest = interests[1]
        PHYSinterest = interests[2]
        BIOLinterest = interests[3]
        CHEMinterest = interests[4]

        self.cosc111 = cosc111
        self.cosc121 = cosc121
        self.math100 = math100
        self.math101 = math101
        self.phys111 = phys111
        self.phys121 = phys121
        self.biol116 = biol116
        self.biol125 = biol125
        self.chem111 = chem111
        self.chem121 = chem121
        self.COSCinterest = COSCinterest
        self.MATHinterest = MATHinterest
        self.PHYSinterest = PHYSinterest
        self.BIOLinterest = BIOLinterest
        self.CHEMinterest = CHEMinterest
        self.loweryearcourses = loweryearcourses
        self.interests = interests
    
    def getGrades(self):
        return self.loweryearcourses
