from dotenv import load_dotenv
import openai, os

load_dotenv();

openai.api_key = os.getenv('OPENAI_API_KEY');

def createCompletion(messages, model='gpt-3.5-turbo'):
    completion = openai.ChatCompletion.create(model=model, messages=messages);

    return completion.choices[0].message.content;