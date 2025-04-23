from loaders.message_loader import MessageLoader
from loaders.connection_loader import ConnectionLoader


class UnifiedLoader:
    def __init__(self, messages_csv_path: str, connections_csv_path: str):
        self.messages_csv_path = messages_csv_path
        self.connections_csv_path = connections_csv_path

    def load(self):
        message_loader = MessageLoader(self.messages_csv_path)
        messages = message_loader.load()

        connection_loader = ConnectionLoader(self.connections_csv_path)
        connections = connection_loader.load()

        # Combine both datasets
        all_documents = messages + connections
        return all_documents
    
    