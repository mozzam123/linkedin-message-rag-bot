# src/retrieval/retriever.py

class Retriever:
    def __init__(self, embedder):
        """
        Initialize the retriever with an embedder instance.
        """
        self.embedder = embedder

    def retrieve(self, query: str, top_k: int = 5):
        """
        Retrieve top_k most relevant documents for the given query.
        """
        if self.embedder.index is None:
            raise ValueError("No FAISS index found. Please embed documents first.")
        
        results = self.embedder.search(query, top_k)
        return results
