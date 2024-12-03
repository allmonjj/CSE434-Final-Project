from Player import Player
from NPC import NPC
from Inventory import Inventory
from Item import Item
from GameMechanics import GameMechanics
from Location import Location


def playerMovement(gm : GameMechanics):
    while True:
        user_input = input("Where to next? (Enter 1 - 4) \n1. NORTH\n2. SOUTH\n3. EAST\n4. WEST\n")
        if user_input == "1":
            gm.moveNorth()
            if gm.checkForEnemy():
                gm.combat()
            if gm.checkForItem():
                # Grab item
                print("Feature not yet implemented")
            break
        elif user_input == "2":
            gm.moveSouth()
            if gm.checkForEnemy():
                gm.combat()
            if gm.checkForItem():
                # Grab item
                print("Feature not yet implemented")
            break
        elif user_input == "3":
            gm.moveEast()
            if gm.checkForEnemy():
                gm.combat()
            if gm.checkForItem():
                # Grab item
                print("Feature not yet implemented")
            break
        elif user_input == "4":
            gm.moveWest()
            if gm.checkForEnemy():
                gm.combat()
            if gm.checkForItem():
                # Grab item
                print("Feature not yet implemented")
            break
        else:
            print("Invalid input. Try again!")

def main():
    print("Welcome to CSE434 Final Project. You will play a Dungeons & Dragons 'esque' game")
    player = Player(100, 0, 0, Inventory(), Location(0, 0, "Beginning Area"))
    gm = GameMechanics(player)
    while True:
        user_input = input("What would you like to do? (Enter 1 - 4) \n1. MOVE\n2. CHECK INVENTORY\n3. LOCATION DETAILS\n4. EXIT\n")
        if user_input == "1":
            playerMovement(gm)
        elif user_input == "2":
            # Check Inventory
            print("Feature not yet defined\n")
        elif user_input == "3":
            # Location Details
            print(player.getCurrLocation().__repr__())
        else:
            print("Thanks for playing!")
            exit()




if __name__ == "__main__":
    main()