import scipy
import requests


class AudioUtils:
    def __init__(self):
        self.API_URL = "https://api-inference.huggingface.co/models/suno/bark-small"

    def query(payload):
	response = requests.post(self.API_URL, headers=headers, json=payload)
	return response.content

    def speak(self, text="Hello World!"):
        print("Model Loaded")
        response = query({
	"inputs": text,
})
        
        scipy.io.wavfile.write("bark_out.wav", rate=response["sampling_rate"], data=response["audio"])
        return response


test_audio = AudioUtils()
output_audio = test_audio.speak(
                                        text = "I'm working on trying out the scripted version of the project to work.")
