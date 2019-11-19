from abc import ABC, abstractmethod
from board import Board


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class DashUpCommand(Command):
    def __init__(self, board: Board):
        self.__board: Board = board
        self.__backupLocation: (int, int) = board.characterLocation()

    def execute(self):
        while self.__board.canMoveUp():
            self.__board.moveUp()

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)


class DashDownCommand(Command):
    def __init__(self, board: Board):
        self.__board: Board = board
        self.__backupLocation: (int, int) = board.characterLocation()

    def execute(self):
        while self.__board.canMoveDown():
            self.__board.moveDown()

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)


class DashLeftCommand(Command):
    def __init__(self, board: Board):
        self.__board: Board = board
        self.__backupLocation: (int, int) = board.characterLocation()

    def execute(self):
        while self.__board.canMoveLeft():
            self.__board.moveLeft()

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)


class DashRightCommand(Command):
    def __init__(self, board: Board):
        self.__board: Board = board
        self.__backupLocation: (int, int) = board.characterLocation()

    def execute(self):
        while self.__board.canMoveRight():
            self.__board.moveRight()

    def undo(self):
        self.__board.teleportCharacter(self.__backupLocation)


class Controller:
    def __init__(self, board: Board):
        self.__board: Board = board
        self.__commandHistory: [Command] = []

    def pressUp(self):
        c = DashUpCommand(self.__board)
        c.execute()
        self.__commandHistory.append(c)

    def pressDown(self):
        c = DashDownCommand(self.__board)
        c.execute()
        self.__commandHistory.append(c)

    def pressLeft(self):
        c = DashLeftCommand(self.__board)
        c.execute()
        self.__commandHistory.append(c)

    def pressRight(self):
        c = DashRightCommand(self.__board)
        c.execute()
        self.__commandHistory.append(c)

    def undo(self):
        self.__commandHistory.pop().undo()


def main():
    b = Board("boardFile2.in")
    c = Controller(b)
    print(b)
    c.pressRight()
    c.pressDown()
    c.pressRight()
    c.pressDown()
    c.pressRight()
    c.pressUp()
    c.pressRight()
    print(b)


if __name__ == "__main__":
    main()
