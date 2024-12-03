import Player
import NPC
import random

class GameMechanics:
    def __init__(self, player):
        if isinstance(player, Player.Player):
            self.player = player

    def combat(self, npc):
        if isinstance(npc, NPC.NPC):
            while self.player.getHp() > 0 and npc.getHp() > 0:
                self.player.setAtkPower(random.randint(1, 6))
                npc.setAtkPower(random.randint(1, 6))
                npc.setHp(npc.getHp() - self.player.getAtkPower())
                print(f"Player HP : {self.player.getHp()} - Player AtkPower : {self.player.getAtkPower()}")
                print(f"NPC HP : {npc.getHp()} - NPC AtkPower : {npc.getAtkPower()}\n")
                if npc.getHp() <= 0:
                    print(f"You have defeated {npc.getName()}!")
                    break
                self.player.setHp(self.player.getHp() - npc.getAtkPower())
                if self.player.getHp() <= 0:
                    print("You have been defeated!")
                    break

    def skillCheck(self, isChallenging):
        if isinstance(isChallenging, bool):
            if isChallenging:
                return True if random.randint(1, 10) >= 6 else False
            else:
                return True if random.randint(1, 10) >= 3 else False

    def levelUp(self):
        if self.player.getXp() >= 50:
            self.player.setHp(self.player.getHp() + 25)
            self.player.setXp(0)