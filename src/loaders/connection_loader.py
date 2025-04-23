import pandas as pd

def load_connections(csv_path: str) -> list:
    df = pd.read_csv(csv_path)
    documents = []

    for idx, row in df.iterrows():
        text = f"Connected with {row['First Name']} {row['Last Name']} on {row['Connected On']} who was as a {row['Position']} in {row['Company']} with Linkedin url: {row['URL']}"

        
        metadata = {
            "type": "connection",
        }

        documents.append({
            "text": text,
            "metadata": metadata
        })

    return documents


