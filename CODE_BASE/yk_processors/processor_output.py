from abc import abstractmethod, ABC
from .process_result import ProcessResult


class ProcessorOutput(ABC):
    @abstractmethod
    def write(self, data: ProcessResult):
        pass