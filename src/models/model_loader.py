from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def load_model():
    model = OpenAIChatCompletionClient(
        model="o4-mini",
        api_key=OPENAI_API_KEY,
    )
    return model