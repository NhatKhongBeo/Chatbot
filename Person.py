class Person:
    def __init__(self, name, age):
        self.name = name
        self.weight = 0
        self.hight = 0
        self.age = age
        self.bmi = 0
        self.intensity = None
        self.phase = None
        
    def setWeight(self, weight):
        self.weight = weight
    def setHight(self, hight):
        self.hight = hight
    def setBMI(self):
        self.bmi = self.computeBMI()
    def setIntensity(self, intensity):
        self.intensity = intensity
    def setPhase(self, phase):
        self.phase = phase
    
    def getName(self):
        return self.name
    def getWeight(self):
        return self.weight
    def getHight(self):
        return self.hight
    def getBMI(self):
        return self.bmi
    
    def computeBMI(self):
        return self.weight / (self.hight * self.hight)
    