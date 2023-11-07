import streamlit as st
import tempfile
from streamlit_webrtc import webrtc_streamer
import av



def upload_video(uploaded_file):
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    video_file_path = tfile.name  # Get the file path of the temporary file

    if "bad" == "bad":
        st.write("Your technique might need improvement in certain areas. Here are some things you can work on or fix.\n" +
                "- Exectue the full range of motion (ROM) to maximize gains\n" +
                "- Avoid leaning into the curl and keep posture upright\n" +
                "- Keep up-and-down motion consistent without moving elbow around\n")
        st.write("Upload a video again if you want to test your new and improved technique.")
    else:
        st.write("Your technique looks accurate and proper. Keep up the good work! Upload a video again if you want to test your curl technique again.")


st.write("DebateMe")

uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "mov", "avi"])
if uploaded_file is not None:
    upload_video(uploaded_file)

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    flipped = img[::-1,:,:]

    return av.VideoFrame.from_ndarray(flipped, format="bgr24")


webrtc_streamer(key="example", video_frame_callback=video_frame_callback)

st.write("TRANSCRIPT");

st.write("Here are some tips to help out!")