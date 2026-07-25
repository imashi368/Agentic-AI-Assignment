import os
import streamlit as st
from agents.router_agent import RouterAgent
from agents.service_agent import ServiceAgent
from agents.verifier_agent import VerifierAgent
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from groq import Groq

st.set_page_config(page_title="GovAssist SL", page_icon="🇱🇰")

st.title("LK GovAssist SL - Agentic AI Government Assistant")


@st.cache_resource
def get_groq_client():
    return Groq(api_key=st.secrets.get("GROQ_API_KEY", "your-groq-api-key-here"))

@st.cache_resource
def load_rag():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    persist_dir = "./chroma_db"
    
    
    if not os.path.exists(persist_dir) or not os.listdir(persist_dir):
        st.info("Building vector database from PDF documents...")
        data_path = "data"
        if os.path.exists(data_path):
            loader = DirectoryLoader(data_path, glob="**/*.pdf", loader_cls=PyMuPDFLoader)
            documents = loader.load()
            
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
            chunks = text_splitter.split_documents(documents)
            
            Chroma.from_documents(
                documents=chunks, 
                embedding=embeddings, 
                persist_directory=persist_dir
            )
        else:
            st.error("Error: 'data' folder not found!")
    
    db = Chroma(persist_directory=persist_dir, embedding_function=embeddings)
    return db.as_retriever()

retriever = load_rag()
groq_client = get_groq_client()


router_agent = RouterAgent(groq_client)
service_agent = ServiceAgent(retriever, groq_client)
verifier_agent = VerifierAgent()

query = st.text_input("Ask your government service question:")

if query:
    
    route = router_agent.route(query)
    st.info(f"Router Agent selected: {route}")

    with st.spinner("Generating response..."):
        
        raw_answer, docs = service_agent.answer(query)
        
        
        final_answer = verifier_agent.verify(raw_answer)

    st.subheader("🤖 AI Response")
    st.success(final_answer)

    st.subheader("📚 Sources")
    if docs:
        for doc in docs:
            st.write(f"- {doc.page_content[:300]}...")
    else:
        st.warning("No relevant sources found in the vector database.")