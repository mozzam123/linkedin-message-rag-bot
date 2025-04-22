# src/vectorstore.py

import faiss
import numpy as np

class VectorStore:
    """
    Stores and searches text embeddings using FAISS.
    """

    def __init__(self, embedding_size):
        """
        Initializes a FAISS index.

        Args:
            embedding_size (int): Dimension of the embedding vectors.
        """
        self.index = faiss.IndexFlatL2(embedding_size)
        self.texts = []  # Store raw texts to retrieve after search

    def add(self, embeddings, texts):
        """
        Adds embeddings and corresponding texts to the store.

        Args:
            embeddings (List[List[float]]): Embedding vectors.
            texts (List[str]): Original text documents.
        """
        np_embeddings = np.array(embeddings).astype('float32')
        self.index.add(np_embeddings)
        self.texts.extend(texts)

    def search(self, query_embedding, top_k=5):
        """
        Searches for top_k most similar documents.

        Args:
            query_embedding (List[float]): The query vector.
            top_k (int): Number of top results to return.

        Returns:
            List[str]: List of top matching text documents.
        """
        query = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query, top_k)
        results = []
        for idx in indices[0]:
            if idx < len(self.texts):
                results.append(self.texts[idx])
        return results
