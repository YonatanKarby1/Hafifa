from fastapi import FastAPI
from abc import ABC, abstractmethod

class APIProcessor(ABC):
    @abstractmethod
    def add_route(self, app: FastAPI):
        pass