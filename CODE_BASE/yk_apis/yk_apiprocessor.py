from fastapi import FastAPI
from abc import ABC, abstractmethod

class yk_APIProcessor(ABC):
    @abstractmethod
    def add_route(self, app: FastAPI):
        pass