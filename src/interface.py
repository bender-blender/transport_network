

from abc import abstractmethod, ABC

class ITransport(ABC):
    """Интерфейс Транспорт

    Args:
        ABC (_type_): _description_

    Raises:
        NotImplementedError: _description_
        NotImplementedError: _description_
    """
    
    @abstractmethod
    def start_engine(self):
        raise NotImplementedError()
    
    @abstractmethod
    def stop_engine(self):
        raise NotImplementedError()