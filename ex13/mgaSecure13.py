from abc import ABC, abstractmethod


class Headline:
    def __init__(self, headline: str, details: str, source: str):
        self.__headline = headline
        self.__details = details
        self.__source = source

    def __str__(self) -> str:
        return "%s (%s)\n" % (self.__headline, self.__source)


class Weather:
    def __init__(self, temp: float, humidity: float, outlook: str):
        self.__temp = temp
        self.__humidity = humidity
        self.__outlook = outlook

    def __str__(self) -> str:
        return "%s: %.1fC %.1f" % (self.__outlook, self.__temp, self.__humidity)


class Subscriber(ABC):
    @abstractmethod
    def update(self, newHeadline: Headline, newWeather: Weather):
        pass


class PushNotifier:
    def __init__(self, headline: Headline, weather: Weather):
        self.__currentWeather = weather
        self.__currentHeadline = headline
        self.__subscribers = []

    def changeHeadline(self, headline: Headline):
        self.__currentHeadline = headline
        self.notifySubscriber()

    def changeWeather(self, weather: Weather):
        self.__currentWeather = weather
        self.notifySubscriber()

    def subscribe(self, subscriber: Subscriber):
        self.__subscribers.append(subscriber)
        subscriber.update(self.__currentHeadline, self.__currentWeather)

    def unsubscribe(self, subscriber: Subscriber):
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)

    def notifySubscriber(self):
        for subscriber in self.__subscribers:
            subscriber.update(self.__currentHeadline, self.__currentWeather)


class EmailSubscriber(Subscriber):
    def __init__(self, emailAddress: str):
        self.__emailAddress = emailAddress
        self.__headline = None
        self.__weather = None

    def update(self, newHeadline: Headline, newWeather: Weather):
        self.__headline = newHeadline
        self.__weather = newWeather
        print("Headline: " + str(self.__headline) +
              "Weather: " + str(self.__weather) + "\n")


class FileLogger(Subscriber):
    def __init__(self, filename: str):
        self.__subject = None
        self.__file = open(filename, "w+")

    def update(self, newHeadline: Headline, newWeather: Weather):
        self.__headline = newHeadline
        self.__weather = newWeather
        self.__file.write("Headline: " + str(self.__headline) +
                          "Weather: " + str(self.__weather) + "\n\n")


def main():
    h = Headline("Dalai Lama Triumphantly Names Successor After Discovering Woman With ‘The Purpose Of Our Lives Is To Be Happy’ Twitter Bio", "Details", "The Onion")
    w = Weather(25.0, 0.7, "Cloudy")
    p = PushNotifier(h, w)
    e = EmailSubscriber("test@gmail.com")
    f = FileLogger("out.out")
    p.subscribe(e)
    p.subscribe(f)
    p.changeHeadline(
        Headline("New Satirical Yet Believable Headline", "New Details", "4chan"))
    p.changeWeather(Weather(25.0, 0.7, "Mega Death"))
    p.unsubscribe(e)
    p.changeHeadline(Headline("Newer Headline", "New Details", "4chan"))
    p.changeWeather(Weather(25.0, 0.7, "Super Mega Death"))


if __name__ == "__main__":
    main()
