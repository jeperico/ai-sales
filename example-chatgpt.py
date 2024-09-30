# ATENTION
# This code is pay-to-win and you need to pay OpenAI API to run it.

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_gpt(prompt: str) -> str:
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "user", "content": prompt}
    ]
  )
  
  return response.choices[0].message.content

prompt = "What is the capital of France?"
answer = ask_gpt(prompt)

print(answer)
