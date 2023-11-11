
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
      {"role": "system", "content": "You are a helpful debate judge designed to output JSON. Make sure that you judge the arguments provided harshly and with constructive criticism"},
      {"role": "user", "content": text}
    ]
  )

  print(response.choices[0].message.content)
  return response.choices[0].message.content