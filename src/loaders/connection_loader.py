import pandas as pd


class ConnectionLoader:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load(self):
        df = pd.read_csv(self.csv_path)
        documents = []

        for idx, row in df.iterrows():

            connection_text = f"Connected with {row['First Name']} {row['Last Name']} on {row['Connected On']} who was as a {row['Position']} in {row['Company']} with Linkedin url: {row['URL']}"

            doc = {
                "id": f"connection-{idx}",
                "text": connection_text
            }

            documents.append(doc)

        return documents




