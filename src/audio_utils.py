import scipy
from transformers import pipeline


class AudioUtils:
    def __init__(self):
        self.suno = pipeline(task='text-to-speech', model='suno/bark')
        self.suno.set_sample_rate(16000)

    def speak(self, text="Hello World!"):
        print("Model Loaded")
        response = self.suno(text)
        scipy.io.wavfile.write("bark_out.wav", rate=response["sampling_rate"], data=response["audio"])
        return response["audio"], response["sampling_rate"]


test_audio = AudioUtils()
output_audio, output_rate = test_audio.speak(text="I'm working on trying out the scripted version of the project to work.")
