import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("AZURE_OPENAI_KEY"),
    base_url = os.getenv("AZURE_OPENAI_ENDPOINT") + "/openai/v1/"
)

def ask_question(messages):
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=messages,
    )

    return response.choices[0].message.content

def main():
    messages = [
        {"role": "user", "content": "Wat is Python?"}
    ]
    answer = ask_question(messages)
    print(answer)

if __name__ == "__main__":
    main()