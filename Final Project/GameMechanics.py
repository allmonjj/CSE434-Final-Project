from AIAPI import AIAPI
from Player import Player
from NPC import NPC
from Location import Location
from Item import Item
import random


class GameMechanics:
    def __init__(self, player):
        if isinstance(player, Player):
            self.player = player
            print(
                f"\nYou enter a room known as {self.player.getCurrLocation().getName()}.\n{self.player.getCurrLocation().getDescription()}\n")
            self.ai = AIAPI()


    def checkForEnemy(self) -> bool:
        return True if self.player.getCurrLocation().getHasEnemy() else False

    def checkForItem(self) -> bool:
        return True if self.player.getCurrLocation().getHasItem() else False

    def combat(self) -> None:
        npc = self.player.getCurrLocation().getNpc()
        if isinstance(npc, NPC):
            print(f"\nAn enemy has appeared! Time to battle!\n\nFoe's Name : {npc.getName()}\n\n{npc.getDescription()}\n")
            print(f"Player HP : {self.player.getHp()} - Player XP : {self.player.getXp()}")
            print(f"NPC HP : {npc.getHp()} - NPC XP : {npc.getXp()}\n")
            origHp = self.player.getHp()
            while self.player.getHp() > 0 and npc.getHp() > 0:
                self.player.setAtkPower(random.randint(1, 6))
                npc.setAtkPower(random.randint(1, 6))

                npc.setHp(npc.getHp() - self.player.getAtkPower())
                if npc.getHp() <= 0:
                    print(f"You have defeated {npc.getName()}!\n")
                    self.player.setHp(origHp)
                    self.player.getCurrLocation().setHasEnemy(False)
                    self.player.getCurrLocation().removeNpc()
                    if npc.getXp() != 0:
                        self.player.setXp(self.player.getXp() + npc.getXp())
                    break

                self.player.setHp(self.player.getHp() - npc.getAtkPower())
                if self.player.getHp() <= 0:
                    print("You have been defeated! Try again soon!")
                    exit()

    def skillCheck(self, isChallenging) -> bool:
        if isinstance(isChallenging, bool):
            if isChallenging:
                return True if random.randint(1, 10) >= 6 else False
            else:
                return True if random.randint(1, 10) >= 3 else False

    def levelUp(self) -> None:
        if self.player.getXp() >= 50:
            print(f"You have leveled up! HP - Old : {self.player.getHp()} New : {self.player.getHp() + 25}\n")
            self.player.setHp(self.player.getHp() + 25)
            self.player.setXp(self.player.getXp() - 50)


    def generateLocation(self):
        if self.player.getCurrLocation().getHasEnemy():
            player_state = {
                "currentLocation": {
                    "coordinates": self.player.getCurrLocation().getCoordinates(),
                    "name": self.player.getCurrLocation().getName(),
                    "description": self.player.getCurrLocation().getDescription(),
                    "hasItem": self.player.getCurrLocation().getHasItem(),
                    "hasEnemy": self.player.getCurrLocation().getHasEnemy(),
                    "npc": {
                        "name": self.player.getCurrLocation().getNpc().getName(),
                        "description": self.player.getCurrLocation().getNpc().getDescription(),
                    }
                }
            }

        else:
            player_state = {
                "currentLocation": {
                    "coordinates": self.player.getCurrLocation().getCoordinates(),
                    "name": self.player.getCurrLocation().getName(),
                    "description": self.player.getCurrLocation().getDescription(),
                    "hasItem": self.player.getCurrLocation().getHasItem(),
                    "hasEnemy": self.player.getCurrLocation().getHasEnemy()
                }
            }

        apiResponse = self.ai.getAPIResponse(player_state=player_state)
        if apiResponse is None:
            print("There was a server error! Sorry, see you soon!")
            exit()
        else:
            response = self.ai.parse_api_response(apiResponse)
            location = response.location
            self.player.getCurrLocation().setName(location.name)
            self.player.getCurrLocation().setDescription(location.description)
            self.player.getCurrLocation().setHasItem(location.hasItem)
            self.player.getCurrLocation().setHasEnemy(location.hasEnemy)

            if location.hasItem:
                self.player.getCurrLocation().setItem(Item(location.item.name, location.item.description, location.item.effect))
            if location.npc:
                self.player.getCurrLocation().addNpc(NPC(location.npc.name, location.npc.description, location.npc.hp, 0, location.npc.xp))

            print(f"You enter a room known as {self.player.getCurrLocation().getName()}.\n{self.player.getCurrLocation().getDescription()}")



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
        print(f"Player has moved East : Current Coordinates : ({x}, {y})\n")
        self.generateLocation()

    def moveWest(self) -> None:
        playCoord = self.player.getCurrLocation().getCoordinates()
        x = playCoord[0] - 1
        y = playCoord[1]
        # Need to specify the following parameters
        # name, description, hasItem, hasEnemy
        self.player.getCurrLocation().setCoordinates((x, y))
        print(f"Player has moved West : Current Coordinates : ({x}, {y})\n")
        self.generateLocation()

    def moveNorth(self) -> None:
        playCoord = self.player.getCurrLocation().getCoordinates()
        x = playCoord[0]
        y = playCoord[1] + 1
        # Need to specify the following parameters
        # name, description, hasItem, hasEnemy
        self.player.getCurrLocation().setCoordinates((x, y))
        print(f"\nPlayer has moved North : Current Coordinates : ({x}, {y})\n")
        self.generateLocation()

    def moveSouth(self) -> None:
        playCoord = self.player.getCurrLocation().getCoordinates()
        x = playCoord[0]
        y = playCoord[1] - 1
        # Need to specify the following parameters
        # name, description, hasItem, hasEnemy
        self.player.getCurrLocation().setCoordinates((x, y))
        print(f"Player has moved South : Current Coordinates : ({x}, {y})\n")
        self.generateLocation()

    def checkInventory(self):
        print(self.player.getInv().__repr__()) # Grabbing inventory object not dictionary here

    def addItemToInventory(self) -> None:
        locItem = self.player.getCurrLocation().getItem()
        user_input = input(f"\nAn item was found in the room!\n\nWould you like to add it to your inventory? (Y?N)\n\nItem Name : {locItem.getName()}\nItem Description : {locItem.getDescription()}\nItem Effect : {locItem.getEffect()}\n").lower()
        if user_input == 'y':
            self.player.getInv().add_Item(locItem)
            self.player.getCurrLocation().removeItem()

    def useItemFromInventory(self) -> None:
        inv = self.player.getInv()
        invLength = len(inv.items)
        user_input = input(f"Which item would you like to use? (1 - {invLength})")

        desiredItem :Item = None

        for i, item in enumerate(inv.items.items(), start=1):
            # Item is considered the tuple, with the Key being an Item object and its value being the count of that item
            if user_input == str(i):
                desiredItem = item[0]
                print(f"\nItem found {item.__repr__()}")
                break
            else:
                continue

        if desiredItem is not None:
            print(f"{desiredItem.getName()} used!\n")
            # USE ITEM LOGIC
            inv.remove_Item(desiredItem)
        else:
            print("Item not found!\n")


