from random import randint
from abc import ABC, abstractmethod


class Monster(ABC):
    @abstractmethod
    def announce(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Bokoblin(Monster):
    @abstractmethod
    def bludgeon(self):
        pass

    @abstractmethod
    def defend(self):
        pass


class NormalBokoblin(Bokoblin):
    def bludgeon(self):
        print("Bokoblin bludgeons you with a boko club for 1 damage")

    def defend(self):
        print("Bokoblin defends itself with a boko shield")

    def announce(self):
        print("A bokoblin appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.bludgeon()
        else:
            self.defend()


class BlueBokoblin(Bokoblin):
    def bludgeon(self):
        print("Blue bokoblin bludgeons you with a spiked boko club for 2 damage")

    def defend(self):
        print("Blue bokoblin defends itself with a spiked boko shield")

    def announce(self):
        print("A blue bokoblin appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.bludgeon()
        else:
            self.defend()


class SilverBokoblin(Bokoblin):
    def bludgeon(self):
        print("Silver bokoblin bludgeons you with a dragonbone boko club for 5 damage")

    def defend(self):
        print("Silver bokoblin defends itself with a dragonbone boko shield")

    def announce(self):
        print("A silver bokoblin appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.bludgeon()
        else:
            self.defend()


class Moblin(Monster):
    @abstractmethod
    def stab(self):
        pass

    @abstractmethod
    def kick(self):
        pass


class NormalMoblin(Moblin):
    def stab(self):
        print("Moblin stabs you with a spear for 3 damage")

    def kick(self):
        print("Moblin kicks you for 1 damage")

    def announce(self):
        print("A moblin appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.stab()
        else:
            self.kick()


class BlueMoblin(Moblin):
    def stab(self):
        print("Blue moblin stabs you with a spear for 5 damage")

    def kick(self):
        print("Blue moblin kicks you for 2 damage")

    def announce(self):
        print("A blue moblin appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.stab()
        else:
            self.kick()


class SilverMoblin(Moblin):
    def stab(self):
        print("Silver moblin stabs you with a spear for 10 damage")

    def kick(self):
        print("Silver moblin kicks you for 3 damage")

    def announce(self):
        print("A silver moblin appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.stab()
        else:
            self.kick()


class Lizalflos(Monster):
    @abstractmethod
    def throwBoomerang(self):
        pass

    @abstractmethod
    def hide(self):
        pass


class NormalLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Lizalflos throws its lizal boomerang at you for 2 damage")

    def hide(self):
        print("Lizalflos camouflages itself")

    def announce(self):
        print("A lizalflos appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.throwBoomerang()
        else:
            self.hide()


class BlueLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Blue lizalflos throws its lizal boomerang at you for 3 damage")

    def hide(self):
        print("Blue lizalflos camouflages itself")

    def announce(self):
        print("A blue lizalflos appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.throwBoomerang()
        else:
            self.hide()


class SilverLizalflos(Lizalflos):
    def throwBoomerang(self):
        print("Silver lizalflos throws its lizal boomerang at you for 7 damage")

    def hide(self):
        print("Silver lizalflos camouflages itself")

    def announce(self):
        print("A silver lizalflos appeared")

    def move(self):
        if randint(1, 3) > 1:
            self.throwBoomerang()
        else:
            self.hide()


class Dungeon(ABC):
    @abstractmethod
    def newBokoblin(self) -> Bokoblin:
        pass

    @abstractmethod
    def newMoblin(self) -> Moblin:
        pass

    @abstractmethod
    def newLizalflos(self) -> Lizalflos:
        pass


class EasyDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return NormalBokoblin()

    def newMoblin(self) -> Moblin:
        return NormalMoblin()

    def newLizalflos(self) -> Lizalflos:
        return NormalLizalflos()


class MediumDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return BlueBokoblin()

    def newMoblin(self) -> Moblin:
        return BlueMoblin()

    def newLizalflos(self) -> Lizalflos:
        return BlueLizalflos()


class HardDungeon(Dungeon):
    def newBokoblin(self) -> Bokoblin:
        return SilverBokoblin()

    def newMoblin(self) -> Moblin:
        return SilverMoblin()

    def newLizalflos(self) -> Lizalflos:
        return SilverLizalflos()


class Encounter:
    def __init__(self, dungeon: Dungeon):
        self.__enemies = []
        for i in range(randint(0, 8)):
            r = randint(1, 3)
            if r == 1:
                self.__enemies.append(dungeon.newBokoblin())
            elif r == 2:
                self.__enemies.append(dungeon.newMoblin())
            else:
                self.__enemies.append(dungeon.newLizalflos())

    def announceEnemies(self):
        print("%d monsters appeared" % len(self.__enemies))
        for enemy in self.__enemies:
            enemy.announce()

    def moveEnemies(self):
        for enemy in self.__enemies:
            enemy.move()


if __name__ == "__main__":
    encounter = Encounter(EasyDungeon())
    # encounter = Encounter(MediumDungeon())
    # encounter = Encounter(HardDungeon())
    encounter.announceEnemies()
    encounter.moveEnemies()
