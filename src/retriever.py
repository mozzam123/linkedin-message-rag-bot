# src/retriever.py

from embedder import Embedder
from vectorstore import VectorStore

class Retriever:
    """
    Retrieves relevant texts from the vector store based on a query.
    """

    def __init__(self, embedder: Embedder, vectorstore: VectorStore):
        """
        Args:
            embedder (Embedder): An instance of the Embedder class.
            vectorstore (VectorStore): An instance of the VectorStore class.
        """
        self.embedder = embedder
        self.vectorstore = vectorstore

    def retrieve(self, query: str, top_k: int = 5):
        """
        Retrieves the top_k most relevant texts for a given query.

        Args:
            query (str): The user's question or input text.
            top_k (int): Number of top results to return.

        Returns:
            List[str]: List of top matching text documents.
        """
        query_embedding = self.embedder.encode([query])[0]
        relevant_texts = self.vectorstore.search(query_embedding, top_k)
        return relevant_texts
