from interface import ITransport
from icecream import ic

class Car(ITransport):
    """
    Машина

    Args:
        ITransport (_type_): _description_
    """
    
    
    def start_engine(self):
        ic("Машина заводится")
    
    def stop_engine(self):
        ic("Машина заглушена")


class Bicycle(ITransport):
    """Велосипед

    Args:
        ITransport (_type_): _description_
    """

    def start_engine(self):
        ic("Велосипед поехал")
    
    def stop_engine(self):
        ic("Велосипед остановился")

class Motorcycle(ITransport):
    """Мотоцикл

    Args:
        ITransport (_type_): _description_
    """
    def start_engine(self):
        ic("Мотоцикл завелся ")
    
    def stop_engine(self):
        ic("Мотоцикл остановился")
