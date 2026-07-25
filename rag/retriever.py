from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")


vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)


retriever = vector_store.as_retriever()

if __name__ == "__main__":
   
    query = "How to apply for a passport?"
    docs = retriever.invoke(query)
    print(f"Found {len(docs)} documents.")
    for i, doc in enumerate(docs):
        print(f"--- Document {i+1} ---")
        print(doc.page_content)