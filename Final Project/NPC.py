class NPC:
    def __init__(self, name, description, hp, atkPower, xp=0):
        self.name = name
        self.description = description
        self.hp = hp
        self.atkPower = atkPower
        self.xp = xp

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def setHp(self, hp):
        self.hp = hp

    def getAtkPower(self):
        return self.atkPower

    def setAtkPower(self, atkPower):
        self.atkPower = atkPower

    def getXp(self):
        return self.xp

    def setXp(self, xp):
        self.xp = xp