
from openai import OpenAI

client = OpenAI()

def processAudio(filePath):
  audio_file = open(filePath, "rb")
  transcript = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      response_format="text"
  )
  return transcript; 

def critiqueSpeech(text):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
      {"role": "system", "content": "You are a helpful debate judge who returns JSON. Your tags are feedback and score. Feedback is a paragrah while score is a number. Make sure that you judge the arguments provided harshly and with constructive criticism. Please also give a rating of the speech out of 10. Demarcate the number by surrounding it with {}"},
      {"role": "user", "content": text}
    ]
  )

  return response.choices[0].message.content

def critiquePairSpeech(speech1, speech2):
  response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },
    messages=[
      {"role": "system", "content": "You are a helpful debate judge who returns JSON. Your tags are feedback and winner. Feedback is a paragrah detailing why you chose the winner of the argument while winner is the number of the speech that won. Make sure that you judge the arguments provided harshly and with constructive criticism."},
      {"role": "user", "content": "speech1: " + speech1 + " speech2: " + speech2}
    ]
  )

  return response.choices[0].message.content
