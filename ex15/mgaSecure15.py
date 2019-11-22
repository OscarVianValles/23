from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def hasNext(self):
        pass


class Collection(ABC):
    @abstractmethod
    def newIterator(self):
        pass


class MyList(Collection):
    def __init__(self, elements):
        self.__elements = elements

    def size(self):
        return len(self.__elements)

    def elementAtIndex(self, index):
        return self.__elements[index]

    def newIterator(self):
        return ReverseIterator(self)


class MyBTree(Collection):
    def __init__(self, value: int, left: 'MyBTree' = None, right: 'MyBTree' = None):
        self.__value = value
        self.__left = left
        self.__right = right

    def left(self):
        return self.__left

    def right(self):
        return self.__right

    def value(self):
        return self.__value

    def newIterator(self):
        return InOrderIterator(self)


class ListIterator(Iterator):
    def __init__(self, list):
        self.__traversedList = list
        self.__currentIndex = 0

    def next(self):
        self.__currentIndex += 1
        return self.__traversedList.elementAtIndex(self.__currentIndex-1)

    def hasNext(self):
        return self.__currentIndex < self.__traversedList.size()


class InOrderIterator(Iterator):
    def __init__(self, MyBTree: 'MyBTree'):
        self.__traversedTree = MyBTree
        self.__stack = []
        self.__visited = []
        if self.__traversedTree is not None:
            self.__stack.append(self.__traversedTree)
            while len(self.__stack) > 0:
                curr = self.__stack[-1]
                if not curr.left() in self.__visited:
                    while curr.left() is not None:
                        self.__stack.append(curr.left())
                        curr = curr.left()

                self.__visited.append(curr)

                if curr.right() is not None:
                    self.__stack.append(curr.right())

                self.__stack.remove(curr)

    def next(self):
        return self.__visited.pop(0).value()

    def hasNext(self):
        return len(self.__visited) > 0


class ReverseIterator(Iterator):
    def __init__(self, list: MyList):
        self.__traversedList = list
        self.__currentIndex = list.size()

    def next(self):
        self.__currentIndex -= 1
        return self.__traversedList.elementAtIndex(self.__currentIndex)

    def hasNext(self):
        return self.__currentIndex > 0


def main():
    c = MyBTree(5, MyBTree(3, right=MyBTree(4)), MyBTree(
        10, MyBTree(8, left=MyBTree(7)), MyBTree(12)))
    c2 = MyList([1, 2, 3, 4])
    i = c.newIterator()
    while i.hasNext():
        print(i.next())


if __name__ == "__main__":
    main()
