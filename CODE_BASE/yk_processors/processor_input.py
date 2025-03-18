from abc import ABC, abstractmethod

from CODE_BASE.yk_processors.process_context import ProcessContext


class ProcessorInput(ABC):
    @abstractmethod
    def read(self) -> ProcessContext:
        pass