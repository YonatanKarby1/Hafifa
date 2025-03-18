from fastapi import FastAPI
from abc import ABC, abstractmethod

class yk_api_processor(ABC):
    @abstractmethod
    def add_route(self, app: FastAPI):
        pass