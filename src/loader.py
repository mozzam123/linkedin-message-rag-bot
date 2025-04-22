import pandas as pd

def load_linkedin_messages(csv_path):
    """
    Loads LinkedIn messages from a CSV file and formats them into small text documents.
    
    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        List[str]: A list of formatted message strings.
    """
    df = pd.read_csv(csv_path)
    documents = []
    
    for _, row in df.iterrows():
        sender = row.get('FROM', 'Unknown Sender')
        receiver = row.get('TO', 'Unknown Receiver')
        date = row.get('DATE', 'Unknown Date')
        content = row.get('CONTENT', '')

        if pd.isna(content) or not content.strip():
            # Skip messages with no content
            continue

        text = f"{date}: {sender} to {receiver} — \"{content}\""
        documents.append(text)

    return documents