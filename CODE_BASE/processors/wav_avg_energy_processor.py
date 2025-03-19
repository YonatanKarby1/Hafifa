from scipy.io import wavfile
import numpy as np
import io

from .multiprocessing_processor import MultiprocessingProcessor


class WavAvgEnergyProcessor(MultiprocessingProcessor):

    def compute_task(self, args: dict) -> any:
        wav_data: io.BytesIO = args['wav_data']
        sample_rate, data = wavfile.read(wav_data)
        data_casted: np.ndarray = data

        if len(data_casted.shape) > 1:
            data_casted = data_casted.mean(axis=1)

        energy = np.square(data_casted)
        average_energy = np.mean(energy)

        return average_energy
