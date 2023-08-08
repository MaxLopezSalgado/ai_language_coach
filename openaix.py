# Import Libraries
import os 
from dotenv import load_dotenv
import openai

openai.api.key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    engine="test-davinci-002"
    prompt="Translate this into Spanish\nwhat rooms do you have available?",
    temperature=0.3, 
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)