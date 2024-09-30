import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

def ask_groq(prompt: str) -> str:
  client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
  )

  chat_completion = client.chat.completions.create(
    messages=[
      {
        "role": "user",
        "content": prompt,
      }
    ],
    model="llama3-8b-8192",
  )

  return chat_completion.choices[0].message.content

prompt = "What is the capital of Honduras?"
answer = ask_groq(prompt)

print(answer)
