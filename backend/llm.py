import os
import time
import openai
from dotenv import load_dotenv
from openai import OpenAIError
from config import LLM_MODEL, MAX_RETRIES, RETRY_DELAY
from typing import List, Optional


class OpenAIChatbot:
    def __init__(self, model: str = LLM_MODEL, max_retries: int = MAX_RETRIES, retry_delay: int = RETRY_DELAY) -> None:
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("Missing OpenAI API key in environment variables.")
        openai.api_key = self.api_key
        self.model = model
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def chat(self, message: str, history: Optional[List[dict]] = None) -> str:
        if history is None:
            history = []
        history.append({"role": "user", "content": message})

        retries = 0
        while retries < self.max_retries:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model, messages=history
                )
                return response["choices"][0]["message"]["content"]
            except OpenAIError as e:
                print(f"Error: {e}. Retrying in {self.retry_delay} seconds...")
                retries += 1
                time.sleep(self.retry_delay)

        raise RuntimeError(
            "Failed to get response from OpenAI API after multiple retries."
        )


# Usage example
if __name__ == "__main__":
    chatbot = OpenAIChatbot()
    response = chatbot.chat("What is the capital of Canada?")
    print(response)
