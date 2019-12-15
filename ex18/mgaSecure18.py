from abc import ABC, abstractmethod

class FileSystemEntity(ABC):
    @abstractmethod
    def size(self) -> float:
        pass

    @abstractmethod
    def searchResults(self,target):
        pass

class Directory(FileSystemEntity):
    def __init__(self, name:str):
        self.__name:str = name;
        self.__children:[FileSystemEntity] = []


    def addChild(self, newChild:FileSystemEntity):
        self.__children.append(newChild)

    def removeChild(self, exChild:FileSystemEntity):
        self__children.remove(exChild) 

    def size(self) -> float:
        size = 0.0
        for child in self.__children:
            size += child.size()
        return size

    def searchResults(self,target:str) -> [FileSystemEntity]:
        results:[FileSystemEntity] = []
        if target == self.__name:
            results.append(self)

        for child in self.__children:
            results.extend(child.searchResults(target)) 

        return results

class File(FileSystemEntity):
    def __init__(self, name:str ,size:float):
        self.__name = name
        self.__size = size

    def size(self) -> float:
        return self.__size

    def searchResults(self,target:str) -> [FileSystemEntity]:
        if target == self.__name:
            return [self]
        else:
            return []

if __name__ == "__main__":
    f = File("file1.txt",5)
    g = File("file2.txt",10)
    h = File("file2.txt",3)
    r = Directory("root")
    s = Directory("innerDir")
    r.addChild(f)
    r.addChild(g)
    r.addChild(s)
    s.addChild(h)
    
    print(r.size())
    print(s.size())
    
    print(f.searchResults("file1.txt"))
