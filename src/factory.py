from dataclasses import dataclass
from interface import ITransport

@dataclass
class Factory:
    """
    Фабрика
    """
    transport: ITransport
    def create_transport(self):
        print(f"{self.transport.__name__} создан")
        return self.transport()