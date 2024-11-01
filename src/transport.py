from interface import ITransport
from icecream import ic

class Car(ITransport):
    """
    Машина

    Args:
        ITransport (_type_): _description_
    """
    
    
    def start_engine(self):
        print("Машина заводится")
    
    def stop_engine(self):
        print("Машина заглушена")


class Bicycle(ITransport):
    """Велосипед

    Args:
        ITransport (_type_): _description_
    """

    def start_engine(self):
        print("Велосипед поехал")
    
    def stop_engine(self):
        print("Велосипед остановился")

class Motorcycle(ITransport):
    """Мотоцикл

    Args:
        ITransport (_type_): _description_
    """
    def start_engine(self):
        print("Мотоцикл завелся ")
    
    def stop_engine(self):
        print("Мотоцикл остановился")
