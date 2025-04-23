# app.py
import os
from dotenv import load_dotenv

from loaders.unified_loader import UnifiedLoader
from embedder import Embedder
from retriever import Retriever
from generator import Generator
from utils import extract_names_from_answer


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ======== Step 1: Load your LinkedIn messages ========

messages_csv = "/home/jidnyasa/Vim/Python/rag_linkedin_bot/data/messages.csv"
connections_csv = "/home/jidnyasa/Vim/Python/rag_linkedin_bot/data/connections.csv"

loader = UnifiedLoader(messages_csv, connections_csv)
documents = loader.load()

print(f"Loaded {len(documents)} documents.")

# ======== Step 2: Embed documents into FAISS ========
embedder = Embedder()
embedder.embed_documents(documents)

print(f"Embedded {len(documents)} documents into FAISS.")

# ======== Step 3: Initialize Retriever ========
retriever = Retriever(embedder)

# ======== Step 4: Initialize Generator ========
generator = Generator(groq_api_key=GROQ_API_KEY)

# ======== Step 5: Define a simple query-answering function ========
def answer_question(user_query: str, top_k: int = 5):
    """
    Answer the user's question using RAG pipeline.
    """
    # Retrieve top relevant documents
    relevant_docs = retriever.retrieve(user_query, top_k=top_k)
    
    # Generate final answer
    final_answer = generator.generate_answer(relevant_docs, user_query)
    
    return final_answer

# ======== Step 6: Interactive loop ========
if __name__ == "__main__":
    print("\n🔍 Welcome to LinkedIn Message Assistant (RAG)")
    print("Type 'exit' to quit.\n")
    
    while True:
        query = input("📝 Your question: ").strip()
        if query.lower() == "exit":
            print("👋 Exiting. Goodbye!")
            break


        relevant_docs = retriever.retrieve(query)
        answer, sources = generator.generate_answer(query, relevant_docs)
        print(f"\n💬 Answer:\n{answer}\n")

        # 🆕 Attribution Part
        print("\n🔗 Sources:")
        mentioned_names = extract_names_from_answer(answer)
        for doc in sources:
            meta = doc.get("metadata", {})
            if meta.get("type") == "message":
                print(f"- Message: Conversation ID {meta.get('conversation_id')} | Folder: {meta.get('folder')}")
            elif meta.get("type") == "connection":
                full_name = meta.get("full_name")
                if full_name and full_name in mentioned_names:
                    print(f"- Connection: {full_name} | Connected on: {meta.get('connected_on')}")  
            else:
                print("- Unknown source type")

