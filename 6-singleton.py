# BUT! singleton pattern is considered an anti-pattern in python

class Singleton:

    __instance = None

    def get_instance(self):
        if self.__instance is None:
            self.__instance = Singleton()
        return self.__instance
