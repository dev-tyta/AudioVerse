import requests
from dotenv import load_dotenv
import os

load_dotenv()

huggingface = os.getenv("HUGGINGFACE")


class AudioUtils:
    def __init__(self):
        self.API_URL = "https://api-inference.huggingface.co/models/suno/bark-small"
        self.headers = {"Authorization": f"Bearer {huggingface}"}

    def query(self, payload):
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        return response.content

    def speak(self, text="Hello World!"):
        print("Model Loaded")
        response = self.query({
            "inputs": text,
        })
        return response


test_audio = AudioUtils()
output_audio = test_audio.speak(text="I'm working on trying out the scripted version of the project to work.")

print(output_audio)
