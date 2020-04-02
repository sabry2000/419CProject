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
    firstyearcourses = []
    interests = []

    def __init__(self, firstyearcourses, interests):
        cosc111 = firstyearcourses[0]
        cosc121 = firstyearcourses[1]
        math100 = firstyearcourses[2]
        math101 = firstyearcourses[3]
        phys111 = firstyearcourses[4]
        phys121 = firstyearcourses[5]
        biol116 = firstyearcourses[6]
        biol125 = firstyearcourses[7]
        chem111 = firstyearcourses[8]
        chem121 = firstyearcourses[9]
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
        self.firstyearcourses = firstyearcourses
        self.interests = interests
    
    def getGrades(self):
        return self.firstyearcourses
