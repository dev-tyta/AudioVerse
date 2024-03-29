import scipy.io.wavfile
import streamlit as st
from src.audio_utils import AudioUtils
import io
import numpy as np


def main():
    st.title("AudioVerse")

    text_input = st.text_input("Enter a text to be transformed", "Hello World")
    audio_utils = AudioUtils()

    if text_input is not None:
        if st.button("Speak"):
            audio_out = audio_utils.speak(text_input)
            audio_data = np.frombuffer(audio_out, dtype=np.int16)
            audio_bytes = io.BytesIO()
            scipy.io.wavfile.write(audio_bytes, rate=44100, data=audio_data)
            audio_bytes.seek(0)

            st.audio(audio_bytes, format="audio/wav")


if __name__ == "__main__":
    main()
