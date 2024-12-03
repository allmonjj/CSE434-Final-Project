class Location:
    def __init__(self, x, y, name=None, description=None, hasItem=False, hasEnemy=False):
        self.coordinates: tuple[int, int] = (x, y)
        self.name = name
        self.description = description
        self.hasItem = hasItem
        self.hasEnemy = hasEnemy

    def getCoordinates(self):
        return self.coordinates

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

    def getHasEnemy(self):
        return self.hasEnemy

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
