from abc import ABC, abstractmethod
from .process_context import ProcessContext

class ComputeProcessor(ABC):

    @abstractmethod
    def process_data(self, context: ProcessContext):
        pass

    def run(self):
        #Get Next job
        #Complate compute of the job
        #Move to next
        pass