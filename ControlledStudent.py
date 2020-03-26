class ControlledStudent:
    def __init__(self, values):
        
        major = values[0]
        cosc111 = values[1]
        cosc121 = values[2]
        cosc222 = values[3]
        math100 = values[4]
        math101 = values[5]
        math200 = values[6]
        phys111 = values[7]
        phys121 = values[8]
        phys216 = values[9]

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
    
    def __call__(self): 
        return self
