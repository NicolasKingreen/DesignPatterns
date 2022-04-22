import random
from time import sleep
from abc import ABC, abstractmethod

# observable registers observers waiting for its update

class IObservable(ABC):
    def __init__(self):
        self.observers = []

    def add(self, observer):
        self.observers.append(observer)

    def remove(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

class WeatherStation(IObservable):

    def __init__(self):
        super().__init__()
        self.sence_temp()  # initializes temp

    def sence_temp(self):
        self.temperature = random.random() * 60 - 30
        self.notify()

# observers wait for observable to notify them

class IObserver(ABC):
    def __init__(self, observable):
        self.observable = observable

    @abstractmethod
    def update(self):
        pass

class Display(IObserver):
    def update(self):
        print(f"Current temperature: {self.observable.temperature:.2f}C")


if __name__ == "__main__":
    weather_station = WeatherStation()
    inside_display = Display(weather_station)
    outside_display = Display(weather_station)

    weather_station.add(inside_display)
    weather_station.add(outside_display)

    weather_station.sence_temp()
    sleep(1)
    weather_station.sence_temp()
    sleep(1)
    weather_station.remove(outside_display)
    weather_station.sence_temp()

