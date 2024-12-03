import Player
import NPC
import Inventory
import Item
import GameMechanics


def main():
    player = Player.Player(100,0, 0, Inventory.Inventory())
    npc = NPC.NPC("Bob", 100, 0)
    gm = GameMechanics.GameMechanics(player)
    gm.combat(npc)

if __name__ == "__main__":
    main()