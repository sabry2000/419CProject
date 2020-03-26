class ExperimentalStudent:
    def __init__(self, values):
        cosc111 = values[0]
        cosc121 = values[1]
        math100 = values[2]
        math101 = values[3]
        phys111 = values[4]
        phys121 = values[5]
        phys112 = values[6]
        phys122 = values[7]
        chem121 = values[8]
        chem123 = values[9]
        MATHinterest = values[10]
        COSCinterest = values[11]
        CHEMinterest = values[12]
        PHYSinterest = values[13]
        BIOLinterest = values[14]

        self.cosc111 = cosc111
        self.cosc121 = cosc121
        self.math100 = math100
        self.math101 = math101
        self.phys111 = phys111
        self.phys121 = phys121
        self.phys112 = phys112
        self.phys122 = phys122
        self.chem121 = chem121
        self.chem123 = chem123
        self.MATHinterest = MATHinterest
        self.COSCinterest = COSCinterest
        self.CHEMinterest = CHEMinterest
        self.PHYSinterest = PHYSinterest
        self.BIOLinterest = BIOLinterest

    def __call__(self): 
        return self
