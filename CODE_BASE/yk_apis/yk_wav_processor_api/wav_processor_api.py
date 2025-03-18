from fastapi import FastAPI
from yk_api_processor import yk_api_processor

class wav_processor(yk_api_processor):

    def __init__(self):
        super().__init__()

    def add_route(self, app: FastAPI):
        
        @app.post("/compute_avg_power")
        def compute_avg_power():
            print("Here")