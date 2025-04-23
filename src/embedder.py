import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle
import os


class Embedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.documents = []
        
    def embed_documents(self, documents: list):
        """
        Embed and add documents into FAISS index.
        """
        texts = [doc['text'] for doc in documents]
        embeddings = self.model.encode(texts, show_progress_bar=True)
        embeddings = np.array(embeddings).astype('float32')

        if self.index is None:
            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)

        self.index.add(embeddings)
        self.documents.extend(documents)
        
    def save_faiss_index(self, index_path: str):
        """
        Save FAISS index and documents metadata.
        """
        if self.index is None:
            raise ValueError("No index to save. Please embed documents first.")
        
        faiss.write_index(self.index, f"{index_path}.faiss")
        
        with open(f"{index_path}_metadata.pkl", "wb") as f:
            pickle.dump(self.documents, f)
            
    def load_faiss_index(self, index_path: str):
        """
        Load FAISS index and documents metadata.
        """
        if not os.path.exists(f"{index_path}.faiss") or not os.path.exists(f"{index_path}_metadata.pkl"):
            raise FileNotFoundError("FAISS index or metadata file not found.")

        self.index = faiss.read_index(f"{index_path}.faiss")
        
        with open(f"{index_path}_metadata.pkl", "rb") as f:
            self.documents = pickle.load(f)
            
    def search(self, query: str, top_k: int = 5):
        """
        Search for the most relevant documents given a query.
        """
        query_embedding = self.model.encode([query]).astype('float32')
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.documents):
                results.append(self.documents[idx])

        return results