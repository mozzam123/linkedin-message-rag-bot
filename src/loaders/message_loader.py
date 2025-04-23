import pandas as pd

def load_messages(csv_path: str) -> list:
    df = pd.read_csv(csv_path)
    documents = []

    for idx, row in df.iterrows():
        # Create a clean text for message
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

    return documents
