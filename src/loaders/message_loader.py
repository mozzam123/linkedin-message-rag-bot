# src/loaders/message_loader.py

import pandas as pd

class MessageLoader:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load(self) -> list:
        """Load messages from a CSV file and return a list of document dictionaries."""
        df = pd.read_csv(self.csv_path)
        documents = []

        for idx, row in df.iterrows():
            # Construct a clean message text
            text = f"From: {row.get('FROM', '')} To: {row.get('TO', '')} On: {row.get('DATE', '')}\n\nMessage:\n{row.get('CONTENT', '')}"

            metadata = {
                "type": "message",  # Important: distinguish document types
                "conversation_id": row.get("CONVERSATION ID", ""),
                "folder": row.get("FOLDER", ""),
                "is_draft": row.get("IS MESSAGE DRAFT", "No")
            }

            documents.append({
                "id": f"message-{idx}",  # Optional: consistent IDs
                "text": text,
                "metadata": metadata
            })

        return documents
