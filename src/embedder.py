from sentence_transformers import SentenceTransformer

class Embedder:
    """
    Encodes text documents into dense vector embeddings using Sentence Transformers.
    """
    
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        """
        Initializes the embedder with a pre-trained model.

        Args:
            model_name (str): Name of the pre-trained model to use.
        """
        self.model = SentenceTransformer(model_name)
        
    
    def encode(self, documents):
        """
        Encodes a list of text documents into embeddings.

        Args:
            documents (List[str]): List of text strings.

        Returns:
            List[List[float]]: List of embedding vectors.
        """
        embeddings = self.model.encode(documents, show_progress_bar=True)
        return embeddings