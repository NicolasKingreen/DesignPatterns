class IBehavior:
    pass

# flying behaviors

class IFlyBehavior(IBehavior):
    def fly(self):
        pass

class IBasicFlying(IFlyBehavior):
    def fly(self):
        print("I'm flying.")

class IJetFlying(IFlyBehavior):
    def fly(self):
        print("Hoo hoo, I'm jet flying!")

# quack behabiors

class IQuackBehavior(IBehavior):
    def quack(self):
        pass

class IBasicQuacking(IQuackBehavior):
    def quack(self):
        print("Quack.")

class ILoudQuacking(IQuackBehavior):
    def quack(self):
        print("QUACK!!")

# client class

class Duck:

    def __init__(self, name, fly_behavior, quack_behavior):
        self.name = name
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def fly(self):
        print(f"[{self.name}]: ", end="")
        self.fly_behavior.fly()

    def quack(self):
        print(f"[{self.name}]: ", end="")
        self.quack_behavior.quack()

class WildDuck(Duck):

    def __init__(self, name):
        super().__init__(name, IBasicFlying(), IBasicQuacking())

class CityDuck(Duck):

    def __init__(self, name):
        super().__init__(name, IBasicFlying(), ILoudQuacking())


if __name__ == "__main__":
    duck1 = WildDuck("Jerry")
    duck2 = CityDuck("Kal")

    duck1.fly()
    duck1.quack()
    duck2.fly()
    duck1.fly()
    duck2.quack()


