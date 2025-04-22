# src/app.py

from loader import load_linkedin_messages
from embedder import Embedder
from vectorstore import VectorStore
from retriever import Retriever
from generator import Generator

def main():
    # Step 1: Load Messages
    messages = load_linkedin_messages(csv_path="data/messages.csv")
    print(f"✅ Loaded {len(messages)} messages.")

    # Step 2: Embed Messages
    embedder = Embedder()
    embeddings = embedder.encode(messages)
    print(f"✅ Embedded {len(embeddings)} messages.")

    # Step 3: Build Vector Store
    embedding_size = len(embeddings[0])  # Get embedding dimension from the first embedding
    vectorstore = VectorStore(embedding_size)
    vectorstore.add(embeddings, messages)
    print("✅ Vector store created.")

    # Step 4: Setup Retriever and Generator
    retriever = Retriever(embedder, vectorstore)
    generator = Generator()

    print("\n🤖 RAG Bot is ready! Ask questions about your LinkedIn messages.\n")
    while True:
        query = input("❓ Enter your question (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("👋 Exiting. Goodbye!")
            break

        # Step 5: Retrieve Relevant Messages
        retrieved_context = retriever.retrieve(query)
        print(f"🔍 Retrieved {len(retrieved_context)} relevant messages.")

        # Step 6: Generate Answer
        answer = generator.generate_answer(query, retrieved_context)
        print(f"\n💬 Answer: {answer}\n")

if __name__ == "__main__":
    main()
