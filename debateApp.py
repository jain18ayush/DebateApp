import streamlit as st
import tempfile
import model
from streamlit_webrtc import webrtc_streamer
import av



def upload_video(uploaded_file):
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    video_file_path = tfile.name  # Get the file path of the temporary file
    model.processAudio(video_file_path)

st.write("DebateMe")

uploaded_file = st.file_uploader("Choose a audio file", type=["mp3", "wav", "m4a"])
if uploaded_file is not None:
    upload_video(uploaded_file)

#For real time streaming 
# def video_frame_callback(frame):
#     img = frame.to_ndarray(format="bgr24")

#     flipped = img[::-1,:,:]

#     return av.VideoFrame.from_ndarray(flipped, format="bgr24")


# webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

st.write("TRANSCRIPT");

st.write("Here are some tips to help out!")