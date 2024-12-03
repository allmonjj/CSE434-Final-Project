class NPC:
    def __init__(self, name, hp, atkPower):
        self.name = name
        self.hp = hp
        self.atkPower = atkPower

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