from abc import ABC, abstractmethod

from .processor_base import ProcessorBase
from multiprocessing import Pool


class MultiprocessingProcessor(ProcessorBase, ABC):

    def __init__(self, degree_of_parallelism: int = 4):
        self.degree_of_parallelism = degree_of_parallelism

    async def process_item_async(self, **kwargs) -> any:
        with Pool(self.degree_of_parallelism) as pool:
            return pool.apply(self.compute_task, args=(kwargs,))

    def process_item(self, **kwargs) -> any:
        with Pool(self.degree_of_parallelism) as pool:
            return pool.apply(self.compute_task, args=(kwargs,))

    @abstractmethod
    def compute_task(self, args: dict) -> any:
        pass

