from fastapi import FastAPI
from ..yk_apiprocessor import yk_APIProcessor

class WavProcessor(yk_APIProcessor):

    def __init__(self):
        super().__init__()

    def add_route(self, app: FastAPI):
        @app.post("/compute_avg_power")
        def compute_avg_power():
            print("Here")