from abc import ABC,abstractmethod

class Fraction:
    def __init__(self,num:int,denom:int):
        self.__num = num
        self.__denom = denom
    def num(self):
        return self.__num
    def denom(self):
        return self.__denom
    def __str__(self) -> str: #so that the str function works implement this
        return str(self.__num) + "/" + str(self.__denom)

class Operation(ABC):
    @abstractmethod
    def execute(self, left:Fraction, right:Fraction) -> 'Fraction':
        pass
    @abstractmethod
    def __str__(self) -> str:
        pass

class Addition(Operation):
    def execute(self, left:Fraction, right:Fraction) -> 'Fraction':
        return Fraction((left.num()*right.denom()) + (right.num()*left.denom()), left.denom() * right.denom())
    def __str__(self) -> str:
        return "+"

class Subtraction(Operation):
    def execute(self, left:Fraction, right:Fraction) -> 'Fraction':
        return Fraction((left.num()*right.denom()) - (right.num()*left.denom()), left.denom() * right.denom())
    def __str__(self) -> str:
        return "-"

class Multiplication(Operation):
    def execute(self, left:Fraction, right:Fraction) -> 'Fraction':
        return Fraction(left.num() * right.num(), left.denom() * right.denom())
    def __str__(self) -> str:
        return "*"
    
class Division(Operation):
    def execute(self, left:Fraction, right:Fraction) -> 'Fraction':
        return Fraction(left.num() * right.denom(), left.denom() * right.num())
    def __str__(self) -> str:
        return "/"
    
class Calculation:
    def __init__(self,left:Fraction,right:Fraction,operation:Operation):
        self.__left = left
        self.__right = right
        self.__operation = operation #the parameter that represents the operation
        self.__answer = operation.execute(left,right) #the answer should be calculated here

    def __str__(self):
        return str(self.__left) + " " + str(self.__operation) + " " + str(self.__right) + " = " + str(self.__answer)
    

