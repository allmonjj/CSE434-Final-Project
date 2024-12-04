from Player import Player
from NPC import NPC
from Location import Location
import random


class GameMechanics:
    def __init__(self, player):
        if isinstance(player, Player):
            self.player = player


    def checkForEnemy(self) -> bool:
        return True if self.player.getCurrLocation().getHasEnemy() else False

    def checkForItem(self) -> bool:
        return True if self.player.getCurrLocation().getHasItem() else False

    def combat(self) -> None:
        npc = self.player.getCurrLocation().getNPC()
        if isinstance(npc, NPC):
            origHp = self.player.getHp()
            while self.player.getHp() > 0 and npc.getHp() > 0:
                self.player.setAtkPower(random.randint(1, 6))
                npc.setAtkPower(random.randint(1, 6))

                print(f"Player HP : {self.player.getHp()} - Player AtkPower : {self.player.getAtkPower()}")
                print(f"NPC HP : {npc.getHp()} - NPC AtkPower : {npc.getAtkPower()}\n")

                npc.setHp(npc.getHp() - self.player.getAtkPower())
                if npc.getHp() <= 0:
                    print(f"You have defeated {npc.getName()}!")
                    self.player.setHp(origHp)
                    break

                self.player.setHp(self.player.getHp() - npc.getAtkPower())
                if self.player.getHp() <= 0:
                    print("You have been defeated!")
                    break

    def skillCheck(self, isChallenging) -> bool:
        if isinstance(isChallenging, bool):
            if isChallenging:
                return True if random.randint(1, 10) >= 6 else False
            else:
                return True if random.randint(1, 10) >= 3 else False

    def levelUp(self) -> None:
        if self.player.getXp() >= 50:
            self.player.setHp(self.player.getHp() + 25)
            self.player.setXp(0)

# Move East / West
    # Modify X coordinate (Left - Right)

# Move North / South
    # Modify Y coordinate (Top - Bottom)

    def moveEast(self) -> None:
        playCoord = self.player.getCurrLocation().getCoordinates()
        x = playCoord[0] + 1
        y = playCoord[1]
        # Need to specify the following parameters
        # name, description, hasItem, hasEnemy
        self.player.getCurrLocation().setCoordinates((x, y))
        print(f"Player has moved East : Current Coordinates : ({x}, {y})")

    def moveWest(self) -> None:
        playCoord = self.player.getCurrLocation().getCoordinates()
        x = playCoord[0] - 1
        y = playCoord[1]
        # Need to specify the following parameters
        # name, description, hasItem, hasEnemy
        self.player.getCurrLocation().setCoordinates((x, y))
        print(f"Player has moved West : Current Coordinates : ({x}, {y})")

    def moveNorth(self) -> None:
        playCoord = self.player.getCurrLocation().getCoordinates()
        x = playCoord[0]
        y = playCoord[1] + 1
        # Need to specify the following parameters
        # name, description, hasItem, hasEnemy
        self.player.getCurrLocation().setCoordinates((x, y))
        print(f"Player has moved North : Current Coordinates : ({x}, {y})")

    def moveSouth(self) -> None:
        playCoord = self.player.getCurrLocation().getCoordinates()
        x = playCoord[0]
        y = playCoord[1] - 1
        # Need to specify the following parameters
        # name, description, hasItem, hasEnemy
        self.player.getCurrLocation().setCoordinates((x, y))
        print(f"Player has moved South : Current Coordinates : ({x}, {y})")