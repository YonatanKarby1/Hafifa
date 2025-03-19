from scipy.io import wavfile
import io

from .multiprocessing_processor import MultiprocessingProcessor


class WavAvgEnergyProcessor(MultiprocessingProcessor):

    def compute_task(self, args: dict) -> any:
        wav_data: bytes = args['wav_data']
        io_stream = io.BytesIO(wav_data)
        sample_rate, data = wavfile.read(io_stream)
        return 0.0
