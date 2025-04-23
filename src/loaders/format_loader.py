# src/loaders/your_loader.py

import pandas as pd

def load_your_data(csv_path: str) -> list:
    """
    Loads [dataset name] data and returns a list of documents for embedding.
    Each document is a dict with 'text' and 'metadata'.
    """
    df = pd.read_csv(csv_path)
    documents = []

    for idx, row in df.iterrows():
        # Build the "text" and "metadata"
        text = f"..."
        metadata = {
            "type": "[dataset-type]",
            "source_id": row.get("some-id"),
            "additional_metadata": "..."
        }
        documents.append({
            "text": text,
            "metadata": metadata
        })
    
    return documents
