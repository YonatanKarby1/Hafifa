import asyncio

from processors.wav_avg_energy_processor import WavAvgEnergyProcessor
from apis import WavProcessor, APIRunner


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    wav_avg_energy_processor = WavAvgEnergyProcessor()
    processor = WavProcessor(wav_avg_energy_processor)
    yk_apirunner = APIRunner(port=8080, hostname="0.0.0.0")
    yk_apirunner.add_api_processor([processor])
    yk_apirunner.run_api()