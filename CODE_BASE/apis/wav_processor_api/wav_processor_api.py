import io

from fastapi import FastAPI, Request
from ..api_processor import APIProcessor
from CODE_BASE.processors import ProcessorBase


class WavProcessor(APIProcessor):

    def __init__(self, processor: ProcessorBase):
        super().__init__()
        self._processor = processor

    @staticmethod
    def _validate_wav(data: io.BytesIO) -> bool:
        header = data.read(4)
        data.seek(0)
        return header == b'RIFF'

    def add_route(self, app: FastAPI):
        @app.post("/compute_avg_energy")
        async def compute_avg_energy(request: Request):
            try:
                wav_data = io.BytesIO(await request.body())
                if not self._validate_wav(wav_data):
                    raise Exception("Provided file is not wav")
                return self._processor.process_item(wav_data=wav_data)
            except Exception as e:
                return {"Error calculating audio energy: ": str(e)}
