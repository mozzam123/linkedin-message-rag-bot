# src/loaders/unified_loader.py

import pandas as pd

class UnifiedLoader:
    def __init__(self, messages_csv: str, connections_csv: str):
        self.messages_csv = messages_csv
        self.connections_csv = connections_csv

    def load(self) -> list:
        documents = []

        # Load messages
        messages_df = pd.read_csv(self.messages_csv)
        for _, row in messages_df.iterrows():
            text = f"From: {row['FROM']} To: {row['TO']} On: {row['DATE']}\n\nMessage:\n{row['CONTENT']}"
            metadata = {
                "type": "message",
                "conversation_id": row.get("CONVERSATION ID"),
                "folder": row.get("FOLDER"),
                "is_draft": row.get("IS MESSAGE DRAFT", "No")
            }
            documents.append({
                "text": text,
                "metadata": metadata
            })

        # Load connections
        connections_df = pd.read_csv(self.connections_csv)
        for _, row in connections_df.iterrows():
            full_name = f"{row['First Name']} {row['Last Name']}".strip()
            text = f"Connection: {full_name}\nPosition: {row['Position']}\nConnected on: {row['Connected On']}"
            metadata = {
                "type": "connection",
                "full_name": full_name,
                "position": row.get("Position"),
                "connected_on": row.get("Connected On")
            }
            documents.append({
                "text": text,
                "metadata": metadata
            })

        return documents
