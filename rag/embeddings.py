import os
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def build_vector_store():
    data_path = "data"
    if not os.path.exists(data_path):
        print("Error: 'data' folder not found!")
        return

    print("Loading documents from 'data/' folder...")
    
    
    loader = DirectoryLoader(
        data_path,
        glob="**/*.pdf",
        loader_cls=PyMuPDFLoader
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} document pages successfully.")

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_documents(documents)
    print(f"Created {len(chunks)} text chunks.")

    print("Generating embeddings and saving to ChromaDB...")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    vector_store = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory="./chroma_db"
    )
    
    print("RAG Vector Store successfully created and saved in './chroma_db'!")

if __name__ == "__main__":
    build_vector_store()