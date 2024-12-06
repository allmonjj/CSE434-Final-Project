from Location import Location
from Inventory import Inventory

class Player():
    def __init__(self, hp, xp, atkPower, inventory : Inventory, currLocation : Location):
        self.hp = hp
        self.xp = xp
        self.atkPower = atkPower
        self.inventory = inventory
        self.currlocation = currLocation

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

    def getInv(self) -> Inventory:
        return self.inventory

    def getAtkPower(self):
        return self.atkPower

    def setAtkPower(self, atkPower):
        self.atkPower = atkPower

    def getCurrLocation(self) -> Location:
        return self.currlocation

    def __repr__(self):
        return f"Player HP : {self.getHp()} - Player ATK Power : {self.getAtkPower()} - Player XP : {self.getXp()}\n"
