import uvicorn
from typing import List
from fastapi import FastAPI
from .yk_apiprocessor import yk_APIProcessor

class yk_APIRunner:

    _app_processors: List[yk_APIProcessor] = []

    def __init__(self, port: int, hostname: str):
        self._app = FastAPI()
        self._port = port
        self._hostname = hostname

    def add_api_processor(self, processors: List[yk_APIProcessor]):
        for processor in processors:
            processor.add_route(self._app)
        self._app_processors.extend(processors)

    def run_api(self):
        uvicorn.run(self._app, port=self._port, host=self._hostname)
