import scipy
from transformers import pipeline


class AudioUtils:
    def __init__(self):
        self.suno = pipeline('text-to-speech', model='suno/bark-small')
        self.suno.set_sample_rate(16000)

    def speak(self, text="Hello World!"):
        response = self.suno(text)
        return response
