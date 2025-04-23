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

    def generate_answer(self, context: list, query: str) -> str:
        """
        Generate an answer based on retrieved context and original query.
        """
        # Build system prompt
        system_prompt = "You are an intelligent assistant. Use the given context to answer the user's question accurately. If you don't know the answer, say you don't know."

        # Combine context documents
        context_text = "\n\n".join([doc['text'] for doc in context])

        # Build messages
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Context:\n{context_text}\n\nQuestion: {query}"}
        ]

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model_name,
            "messages": messages,
            "temperature": 0.2
        }

        response = requests.post(self.endpoint, headers=headers, json=payload)

        if response.status_code != 200:
            raise Exception(f"Groq API Error: {response.status_code} {response.text}")

        result = response.json()
        answer = result['choices'][0]['message']['content'].strip()
        return answer
