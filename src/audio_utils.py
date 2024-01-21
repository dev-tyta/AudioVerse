import scipy
from transformers import pipeline


class AudioUtils:
    def __init__(self):
        self.suno = pipeline('text-to-speech', model='suno/bark-small')
        self.suno.set_sample_rate(16000)


