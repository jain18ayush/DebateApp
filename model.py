
from openai import OpenAI
from dotenv import load_dotenv
import os


def load_env_variables(env_file):
    with open(env_file) as f:
        for line in f:
            if line.startswith('#') or not line.strip():
                # Skip comments and empty lines
                continue
            # Parse the key-value pair and set it as environment variable
            key, value = line.strip().split('=', 1)
            os.environ[key] = value

env_file_path = '.env'
load_env_variables(env_file_path)

client = OpenAI(os.getenv('OPENAI_API_KEY'))

def processAudio(filePath):
  audio_file = open(filePath, "rb")
  transcript = client.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      response_format="text"
  )

  print(transcript);
  return transcript; 



