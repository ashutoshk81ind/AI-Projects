import os
import time
from dotenv import load_dotenv
from openai import AzureOpenAI
# Load .env variables
load_dotenv()
# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)
while True:
    user_message=input("Enter your message:(or type 'quit'): ")
    if user_message.lower() == 'quit':
        break
    if not user_message.strip():
        print("Please enter a valid message.")
        continue
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that responds to user queries.",
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
    )
    print("Response:", response.choices[0].message.content)
   