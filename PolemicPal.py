import streamlit as st
import tempfile
import model
import json
import os

# Initialize the session state for storing scores if it's not already initialized
if 'scores' not in st.session_state:
    st.session_state.scores = []


def upload_audio(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.m4a') as tfile:
        tfile.write(uploaded_file.read())
        temp_file_path = tfile.name  # Get the file path of the temporary file

    # Process the audio file
    result = model.processAudio(temp_file_path)
    critique = model.critiqueSpeech(result)
    json_data = json.loads(critique)

    st.subheader("Transcript:")
    st.write(result)
    st.subheader("Feedback:")
    # Display feedback in a box
    st.info(json_data["feedback"])

    # Append the score to the session state list
    st.session_state.scores.append(json_data["score"])

    # Clean up the temporary file
    os.remove(temp_file_path)


st.title("PolemicPal")
st.info("A place to debate a bot as well as your friends! Improve and grow with tailored advice from the world's foremost large language model ChatGPT.")
st.divider()
st.subheader("Customize the feedback: ")

# Creating columns with additional spacer columns
col1, spacer1, col2, spacer2, col3, spacer3, col4 = st.columns(
    [1, 0.2, 1, 0.2, 1, 0.2, 1])

with col1:
    st.button("😊 Facial Expressions")

with col2:
    st.button("🕺 Body Movements")

with col3:
    st.button("👌 Sign & Voice Clarity")

with col4:
    st.button("🎤 Vocal Analysis")

col5, spacer1, col6, spacer2, col7, spacer3, col8 = st.columns(
    [1, 0.2, 1, 0.2, 1, 0.2, 1])
with col5:
    st.button("🧑‍⚖️ Lincoln-Douglas")
with col6:
    st.button("👥 Public Forum")
with col7:
    st.button("🗣️ Speech")
with col8:
    st.button("🏛️ Congress")


st.caption("Upload an audio file or a video file of you practicing a speech.")
uploaded_file = st.file_uploader("", type=["mp3", "wav", "m4a", "mp4"])
if uploaded_file is not None:
    upload_audio(uploaded_file)
    total_score = sum(st.session_state.scores)
    st.write(f"Speech Score: {st.session_state.scores[-1]}")
    st.write(f"Total Score: {total_score}")

if st.button('Reset Scores'):
    del st.session_state['scores']  # Reset only the scores
    # OR
    # for key in list(st.session_state.keys()):
    #     del st.session_state[key]  # Reset the entire session state
    st.write('Scores reset!')
