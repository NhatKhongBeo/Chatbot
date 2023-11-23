class Person:
    def __init__(self):
        self.name = None
        self.weight = 0
        self.hight = 0
        self.age = None
        self.bmi = 0
        self.intensity = None
        self.phase = None

    def setWeight(self, weight):
        self.weight = weight

    def setHight(self, hight):
        self.hight = hight/100

    def setBMI(self):
        self.bmi = self.computeBMI()

    def setIntensity(self, intensity):
        self.intensity = intensity

    def setPhase(self, phase):
        self.phase = phase

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getHight(self):
        return self.hight

    def getBMI(self):
        return self.bmi

    def getIntensity(self):
        return self.intensity

    def getPhase(self):
        return self.phase

    def computeBMI(self):
        return self.weight / (self.hight * self.hight)
