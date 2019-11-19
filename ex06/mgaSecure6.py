# returnItem(b:BorrowableItem): : returns nothing, it removes the BorrowableItem, b from the __borrowedItems attribute.
# penalty(b:BorrowableItem,today:Date):float : returns a float which is the calculated penalty for BorrowableItem, b when returned today. Every day after the due date the penalty increases by 3.5. An item which is overdue for 4 days has a penalty of 14.
# itemsDue(today:Date):[BorrowableItem] : returns a list of BorrowableItems which are on or past the due date. The due date for a Book is 7 days, a Periodical is 1 day, and a PC is 0 days.
# totalPenalty(today:Date):float : returns a float which is the total penalty for all the overdue books when calculated today

from abc import ABC, abstractmethod

class Date:
    def __init__(self, month:int, day:int, year:int):
        self.__month = month
        self.__day = day
        self.__year = year

    def mdyFormat(self) -> str:
        return str(self.__month) + "/" + str(self.__day) + "/" + str(self.__year)

    def days(self) -> int:
        months:[int] = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
        days:int = self.__year * 365

        for i in range(self.__month):
            days += months[i]

        days += self.__day

        return days

    def dateDifference(self, otherDate:'Date') -> int:
        return otherDate.days() - self.days()


class Page:
    def __init__(self, sectionHeader:str, body: str):
        self.__sectionHeader = sectionHeader
        self.__body = body


class BorrowableItem(ABC):
    @abstractmethod
    def uniqueItemId(self) -> int:
        pass

    @abstractmethod
    def commonName(self) -> str:
        pass


class Book(BorrowableItem):
    def __init__(self, bookId:int, title:str, author:str, publishDate:Date, pages: [Page]):
        self.__bookId = bookId
        self.__title = title
        self.__publishDate = publishDate
        self.__author = author
        self.__pages = pages

    def coverInfo(self) -> str:
        return "Title: " + self.__title + "\nAuthor: " + self.__author

    def uniqueItemId(self) -> int:
        return self.__bookId

    def commonName(self) -> str:
        return "Borrowed Item:" + self.__title + " by " + self.__author


class LibraryCard:
    def __init__(self, idNumber: int, name: str, borrowedItems: {BorrowableItem:Date}):
        self.__idNumber = idNumber
        self.__name = name
        self.__borrowedItems = borrowedItems

    def borrowItem(self,book:BorrowableItem, date:Date):
        self.__borrowedItems[book] = date

    def borrowerReport(self) -> str:
        r:str = self.__name + "\n"
        for borrowedItem in self.__borrowedItems:
            r = r + borrowedItem.commonName() + ", borrow date: " + self.__borrowedItems[borrowedItem].mdyFormat() + "\n"
        return r

    def returnItem(self, b:BorrowableItem):
        if b in self.__borrowedItems:
            del self.__borrowedItems[b]

    def penalty(self, b:BorrowableItem, today:Date) -> float:
        if b in self.__borrowedItems:
            maxTime:int = 0
            if isinstance(b, Book):
              maxTime = 7
            elif isinstance(b, Periodical):
              maxTime = 1

            daysOverdue = self.__borrowedItems[b].dateDifference(today) - maxTime
            return 0 if daysOverdue < 0 else daysOverdue * 3.5

    def itemsDue(self, today:Date) -> [BorrowableItem]:
      dueItems:[BorrowableItem] = []
      for b in self.__borrowedItems:
        maxTime:int = 0
        if isinstance(b, Book):
          maxTime = 7
        elif isinstance(b, Periodical):
          maxTime = 1
        if self.__borrowedItems[b].dateDifference(today) > maxTime:
          dueItems = dueItems + [b]
      return dueItems

    def totalPenalty(self, today:Date) -> float:
      penalties:float = 0.0
      for b in self.__borrowedItems:
        penalties += self.penalty(b, today)
      return penalties


class Periodical:
    def __init__(self, __periodicalID:int, __title:str, __issue:Date, __pages:[Page]):
        self.__periodicalID = __periodicalID
        self.__title = __title
        self.__issue = __issue
        self.__pages = __pages

    def uniqueItemId(self) -> int:
        return self.__periodicalID

    def commonName(self) -> str:
        return self.__title + " " + self.__issue.mdyFormat()


class PC:
    def __init__(self, __pcID:int):
        self.__pcID = __pcID

    def uniqueItemId(self) -> int:
        return self.__pcID

    def commonName(self) -> str:
        return "PC" + str(self.__pcID)


tomorrowsDate = Date(10, 2, 2019)
todaysDate = Date(10, 1, 2019)

lc = LibraryCard(123, "Thomas", {})
p = Periodical(911, "Hello", tomorrowsDate, [])
b = PC(678)
book = Book(123, "Test", "Cool", Date(9, 9, 1999), [])
lc.borrowItem(b, todaysDate)
lc.borrowItem(p, todaysDate)
lc.borrowItem(book, Date(9,29,2019))

print(lc.penalty(book, Date(10,7,2019)))
# nextDate = Date(10,3,2019)
# borrowedItems = lc.itemsDue(nextDate)
# for i in borrowedItems:
#     print(i.commonName())
#
# print(lc.totalPenalty(nextDate))
