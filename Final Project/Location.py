from NPC import NPC
from Item import Item

class Location:
    def __init__(self, x, y, name : str =None, description : str=None, hasItem=False, hasEnemy=False, npc : NPC=None, item : Item=None):
        self.coordinates: tuple[int, int] = (x, y)
        self.name = name
        self.description = description
        self.hasItem = hasItem
        self.hasEnemy = hasEnemy
        self.npc = npc
        self.item = item

    def getCoordinates(self):
        return self.coordinates

    def setCoordinates(self, coordinates : tuple[int, int]):
        self.coordinates = coordinates

    def getX(self):
        return self.coordinates[0]

    def getY(self):
        return self.coordinates[1]

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def getHasItem(self):
        return self.hasItem

    def setHasItem(self, hasItem : bool):
        self.hasItem = hasItem

    def getHasEnemy(self):
        return self.hasEnemy

    def setHasEnemy(self, hasEnemy : bool):
        self.hasEnemy = hasEnemy

    def getNpc(self) -> NPC:
        return self.npc

    def setNpc(self, npc : NPC):
        self.npc = npc

    def getItem(self) -> Item:
        return self.item

    def removeItem(self):
        self.item = None

    def __repr__(self):
        return (
            f"Location\n"
            f"  Coordinates   : {self.coordinates}\n"
            f"  Name          : {self.name}\n"
            f"  Description   :\n"
            f"    {self.description}\n\n"
            f"  Item          : {self.hasItem}\n"
            f"  Enemy         : {self.hasEnemy}\n"
        )
