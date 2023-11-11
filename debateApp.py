import streamlit as st
import tempfile
import model
from streamlit_webrtc import webrtc_streamer
import av


import tempfile
import shutil
import os


def upload_audio(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.m4a') as tfile:
        tfile.write(uploaded_file.read())
        temp_file_path = tfile.name  # Get the file path of the temporary file

    # Process the audio file
    result = model.processAudio(temp_file_path)
    st.write(result)
    critique = model.critiqueSpeech(result)
    st.write( "\n" + critique)

    # Clean up the temporary file
    os.remove(temp_file_path)


st.write("DebateMe")

uploaded_file = st.file_uploader(
    "Choose a audio file", type=["mp3", "wav", "m4a"])
if uploaded_file is not None:
    upload_audio(uploaded_file)