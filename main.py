import scipy.io.wavfile
import streamlit as st
from src.audio_utils import AudioUtils
import io


def main():
    st.title("AudioVerse")

    text_input = st.text_input("Enter a text to be transformed", "Hello World")
    audio_utils = AudioUtils()

    if text_input is not None:
        if st.button("Speak"):
            audio_out = audio_utils.speak(text_input)
            audio_bytes = io.BytesIO()
            scipy.io.wavfile.write(audio_bytes, data=audio_out)
            audio_bytes.seek(0)

            st.audio(audio_bytes, format="audio/wav")


if __name__ == "__main__":
    main()
