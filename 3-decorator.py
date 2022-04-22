from abc import ABC, abstractmethod

class Beverage(ABC):

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def cost(self):
        pass

# decorators have beverage and are also beverages

class TopingDecorator(Beverage, ABC):

    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description()

class CaramelDecorator(TopingDecorator):

    def cost(self):
        return self.beverage.cost() + 19

class ChocolateDecorator(TopingDecorator):

    def cost(self):
        return self.beverage.cost() + 29

# common beverages

class Espresso(Beverage):

    def get_description(self):
        return """
            Espresso is a coffee-brewing method of Italian origin,
            in which a small amount of nearly boiling water (about 90 °C or 190 °F)
            is forced under 9–10 bars (900–1,000 kPa; 130–150 psi)
            of pressure through finely-ground coffee beans.
            Espresso coffee can be made with a wide
            variety of coffee beans and roast degrees.
            Espresso is the most common way of making coffee in southern Europe,
            especially in Italy, France, Spain and Portugal.
            It is also popular in Switzerland, Croatia,
            Bulgaria and Greece, and in Australia.
        """

    def cost(self):
        return 79

class Decaf(Beverage):

    def get_description(self):
        return """
            Decaf is short for decaffeinated coffee.
            It's coffee from coffee beans that have had
            at least 97% of their caffeine removed.
        """

    def cost(self):
        return 89


if __name__ == "__main__":
    my_order = Espresso()
    my_order = CaramelDecorator(my_order)
    print(f"Final cost: {my_order.cost()}")
    print(f"Description: {my_order.get_description()}")
