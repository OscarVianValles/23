from abc import ABC, abstractmethod


class SearchAlgorithm(ABC):
    def __init__(self, target: int, searchSpace: [int]):
        self._searchSpace = searchSpace
        self._currentIndex = 0
        self._solutions = []
        self._target = target

    def bruteForceSolution(self):
        candidate = self.first()
        while(self.isSearching()):
            if self.isValid(candidate):
                self.updateSolution(candidate)
            candidate = self.next()
        return self._solutions

    def first(self) -> int:
        return self._searchSpace[0]

    def next(self) -> int:
        self._currentIndex += 1
        if self.isSearching():
            return self._searchSpace[self._currentIndex]

    def isSearching(self) -> bool:
        return self._currentIndex < len(self._searchSpace)

    @abstractmethod
    def isValid(self, candidate) -> bool:
        pass

    @abstractmethod
    def updateSolution(self, candidate):
        pass


class EqualitySearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate) -> bool:
        return candidate == self._target

    def updateSolution(self, candidate):
        self._solutions.append(candidate)


class DivisibilitySearchAlgorithm(SearchAlgorithm):
    def isValid(self, candidate) -> bool:
        return candidate % self._target == 0

    def updateSolution(self, candidate):
        self._solutions.append(candidate)


class MinimumSearchAlgorithm(SearchAlgorithm):
    def __init__(self, target: int, searchSpace: [int]):
        self._searchSpace = searchSpace
        self._currentIndex = 0
        self._solutions = [searchSpace[0]]
        self._target = target

    def first(self) -> int:
        return self._searchSpace[1]

    def isValid(self, candidate) -> bool:
        return candidate < self._solutions[0]

    def updateSolution(self, candidate):
        self._solutions[0] = candidate


def main():
    e = EqualitySearchAlgorithm(2, [4, 2, 3, 6, 1, 5, 2])
    print(e.bruteForceSolution())
    e = DivisibilitySearchAlgorithm(2, [4, 2, 3, 6, 1, 5, 2])
    print(e.bruteForceSolution())
    e = MinimumSearchAlgorithm(None, [2, 3, 1, 0, 6, 2, 4])
    print(e.bruteForceSolution())


if __name__ == "__main__":
    main()
