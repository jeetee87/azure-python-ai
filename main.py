import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("AZURE_OPENAI_KEY"),
    base_url = os.getenv("AZURE_OPENAI_ENDPOINT") + "/openai/v1/"
)

def ask_question(user_input):
    response = client.chat.completions.create(
    model = os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages = [
        {
            "role": "user", "content": user_input
        }
    ],
)
    return response.choices[0].message.content

def main():
    user_input = input("Stel je vraag?")
    answer = ask_question(user_input=user_input)
    print(answer)
    
if __name__ == "__main__":
    main()