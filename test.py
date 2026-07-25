from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

print("Loading embeddings model...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Loading Chroma DB from './chroma_db'...")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = db.as_retriever()

print("Searching for documents...")
docs = retriever.invoke("How to apply for a new passport?")

print(f"\n--- Result Found: {len(docs)} documents ---")
for i, d in enumerate(docs):
    print(f"\n[Doc {i+1}]:\n{d.page_content[:300]}...")