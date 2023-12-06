import streamlit as st
import tempfile
import model
import json
import os

# Initialize the session state for storing scores if it's not already initialized
if 'scores' not in st.session_state:
    st.session_state.scores = []


def upload_and_process_audio(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix='.m4a') as tfile:
        tfile.write(uploaded_file.read())
        temp_file_path = tfile.name  # Get the file path of the temporary file

    result = model.processAudio(temp_file_path)
    os.remove(temp_file_path)
    return result


st.title("Debate a Friend!")

uploaded_file_1 = st.file_uploader("Upload first speech", type=[
                                   "mp3", "wav", "m4a", "mp4"])
uploaded_file_2 = st.file_uploader("Upload second speech", type=[
                                   "mp3", "wav", "m4a", "mp4"])

if uploaded_file_1 and uploaded_file_2:
    result_1 = upload_and_process_audio(uploaded_file_1)
    result_2 = upload_and_process_audio(uploaded_file_2)    
    # Create two columns for the transcripts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("First Speech Transcript:")
        st.write(result_1)
        json_data = json.loads(model.critiqueSpeech(result_1))
        st.subheader("Feedback")
        st.write(json_data["feedback"])
        st.write(f"Speech Score: {json_data['score']}")

    with col2:
        st.subheader("Second Speech Transcript:")
        st.write(result_2)
        json_data = json.loads(model.critiqueSpeech(result_2))
        st.subheader("Feedback")
        st.write(json_data["feedback"])
        st.write(f"Speech Score: {json_data['score']}")


    # Concatenate the results for critique
    concatenated_result = result_1 + " " + result_2
    critique = model.critiquePairSpeech(result_1, result_2)
    json_data = json.loads(critique)

    # Displaying critique and feedback
    st.subheader("Judgement:")
    st.info(json_data["feedback"])
    st.subheader(f"The victor is Debater  {json_data['winner']}!")

if st.button('Reset Scores'):
    del st.session_state['scores']
    st.write('Scores reset!')
