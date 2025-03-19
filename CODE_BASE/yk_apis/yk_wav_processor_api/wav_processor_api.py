from fastapi import FastAPI, Request
from ..yk_apiprocessor import yk_APIProcessor
from CODE_BASE.yk_processors import ProcessorBase


class WavProcessor(yk_APIProcessor):

    def __init__(self, processor: ProcessorBase):
        super().__init__()
        self._processor = processor

    def add_route(self, app: FastAPI):
        @app.post("/compute_avg_energy")
        async def compute_avg_energy(request: Request):
            wav_data = await request.body()
            # Validate that the file is wav

            # Perform the calculation
            return self._processor.process_item(wav_data=wav_data)
