# src/generator.py

import os
import groq  # 👉 Using Groq's SDK now
from dotenv import load_dotenv

load_dotenv()

class Generator:
    """
    Generates an answer using Groq API models based on retrieved context.
    """

    def __init__(self, model_name="llama3-70b-8192", temperature=0.2):
        """
        Args:
            model_name (str): Name of the Groq model to use.
            temperature (float): Sampling temperature (0 = deterministic).
        """
        self.model_name = model_name
        self.temperature = temperature
        self.client = groq.Groq(
            api_key=os.getenv("GROQ_API_KEY")  # 🚨 Environment Variable: GROQ_API_KEY
        )

    def generate_answer(self, query: str, context: list[str]) -> str:
        """
        Generates an answer based on the query and provided context.

        Args:
            query (str): The user's input question.
            context (list[str]): Retrieved related texts/messages.

        Returns:
            str: Groq-generated answer.
        """
        prompt = self._build_prompt(query, context)

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant summarizing and answering based on past LinkedIn conversations."},
                {"role": "user", "content": prompt}
            ],
            temperature=self.temperature,
            max_tokens=500,
        )

        answer = response.choices[0].message.content
        return answer

    def _build_prompt(self, query: str, context: list[str]) -> str:
        """
        Builds the prompt that will be sent to Groq.

        Args:
            query (str): The user's input question.
            context (list[str]): Retrieved texts.

        Returns:
            str: Final prompt.
        """
        joined_context = "\n\n".join(context)
        prompt = f"""
Here are some past LinkedIn conversations:
{joined_context}

Using only the information from these conversations, please answer the following question:

{query}
"""
        return prompt.strip()
