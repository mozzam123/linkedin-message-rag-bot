# src/generator/generator.py

import requests
import os

class Generator:
    def __init__(self, groq_api_key: str, model_name: str = "llama3-8b-8192"):
        """
        Initialize Generator with Groq API key and model name.
        """
        self.api_key = groq_api_key
        self.model_name = model_name
        self.endpoint = "https://api.groq.com/openai/v1/chat/completions"

    def generate_answer(self, question: str, documents: list) -> str:

        context = "\n\n".join(doc["text"] for doc in documents)

        prompt = f"""You are a helpful assistant. Use the below context to answer the question.

        Context:
        {context}

        Question:
        {question}

            Answer:"""

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model_name,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2
        }

        
        response = requests.post(self.endpoint, headers=headers, json=payload)
        if response.status_code != 200:
            raise Exception(f"Groq API Error: {response.status_code} {response.text}")

        result = response.json()
        answer = result['choices'][0]['message']['content'].strip()

        return answer, documents  # ⬅️ now returns both answer + sources
