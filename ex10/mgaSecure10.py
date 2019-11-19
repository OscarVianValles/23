from abc import ABC,abstractmethod

class State(ABC):
    @abstractmethod
    def compress(self):
        pass
    @abstractmethod
    def release(self):
        pass
    @abstractmethod
    def cool(self):
        pass
    @abstractmethod
    def heat(self):
        pass
    
class SolidState(State):
    def __init__(self, matter:'Matter'):
        self.__matter = matter
    def compress(self):
        print("Compressing")
    def release(self):
        print("Releasing")
        self.__matter.changeState(LiquidState(self.__matter))
    def cool(self):
        print("Cooling")
    def heat(self):
        print("Heating")
        self.__matter.changeState(LiquidState(self.__matter))
    def __str__(self):
        return "solid"
        
class LiquidState(State):
    def __init__(self, matter:'Matter'):
        self.__matter = matter
    def compress(self):
        print("Compressing")
        self.__matter.changeState(SolidState(self.__matter))
    def release(self):
        print("Releasing")
        self.__matter.changeState(GaseousState(self.__matter))
    def cool(self):
        print("Cooling")
        self.__matter.changeState(SolidState(self.__matter))
    def heat(self):
        print("Heating")
        self.__matter.changeState(GaseousState(self.__matter))
    def __str__(self):
        return "liquid"
        
class GaseousState(State):
    def __init__(self, matter:'Matter'):
        self.__matter = matter
    def compress(self):
        print("Compressing")
        self.__matter.changeState(LiquidState(self.__matter))
    def release(self):
        print("Releasing")
    def cool(self):
        print("Cooling")
        self.__matter.changeState(LiquidState(self.__matter))
    def heat(self):
        print("Heating")
    def __str__(self):
        return "gas"

class Matter:
    def __init__(self,name:str):
        self.__name = name
        self.__state = LiquidState(self) #change this to the appropriate initial state (liquid)
    def changeState(self,newState):
        self.__state = newState
    def compress(self):
        self.__state.compress()
    def release(self):
        self.__state.release()
    def cool(self):
        self.__state.cool()
    def heat(self):
        self.__state.heat()
    def __str__(self):
        return "%s is currently a %s" % (self.__name,self.__state)
