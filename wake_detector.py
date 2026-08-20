import numpy as np
import pyaudio
from openwakeword.model import Model

class WakeWordDetector:
    def __init__(self, keyword="hey_jarvis"):
        self.model = Model(wakeword_models=["hey_jarvis"], inference_framework="onnx")
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(
            rate=16000,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=1280
        )

    def wait_for_wake_word(self) -> bool:
        while True:
            audio = np.frombuffer(self.audio_stream.read(1280, exception_on_overflow=False), dtype=np.int16)
            prediction = self.model.predict(audio)
            for _, score in prediction.items():
                if score >= 0.5:
                    return True

    def close(self):
        if self.audio_stream:
            self.audio_stream.close()
        if self.pa:
            self.pa.terminate()