from dataclasses import dataclass
from interface import ITransport
from icecream import ic

@dataclass
class Factory:
    """
    Фабрика
    """
    transport: ITransport
    ic("Фабрика")
    def create_transport(self):
        ic(f"{self.transport.__name__} создан")
        return self.transport()