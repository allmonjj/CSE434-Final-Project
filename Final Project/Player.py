class Player():
    def __init__(self, hp, xp, atkPower, inventory):
        self.hp = hp
        self.xp = xp
        self.atkPower = atkPower
        self.inventory = inventory

    def getId(self):
        return self.id

    def getHp(self):
        return self.hp

    def setHp(self, hp):
        self.hp = hp

    def getXp(self):
        return self.xp

    def setXp(self, xp):
        self.xp = xp

    def getInv(self):
        return self.inventory

    def getAtkPower(self):
        return self.atkPower

    def setAtkPower(self, atkPower):
        self.atkPower = atkPower
