from abc import ABC, abstractmethod


class ProcessorBase(ABC):
    @abstractmethod
    def process_item(self, **kwargs) -> any:
        pass

    @abstractmethod
    async def process_item_async(self, **kwargs) -> any:
        pass