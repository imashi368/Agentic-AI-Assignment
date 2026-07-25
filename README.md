## Retrieval Evaluation

I tested my RAG pipeline with 5 sample queries to evaluate the relevance and accuracy of the retrieved context and generated responses:

1. **Query:** What are the instructions and requirements for applying for dual citizenship in Sri Lanka?
   - **Retrieved Context Relevance:** High. Successfully retrieved official guidelines and application requirements from dual_instructions_english.pdf and DualCIT_Application.pdf
   - **Generated Answer Accuracy:** Accurate and aligned with official department guidelines.

2. **Query:** What are the guidelines and application procedures for obtaining a multiple-entry visa?
   - **Retrieved Context Relevance:** High. Extracted exact clauses and conditions from multiple_entry_visa.pdf
   - **Generated Answer Accuracy:** Clear and well-synthesized by the agent.

3. **Query:** What are the requirements and rules for opening a pre-payment account?
   - **Retrieved Context Relevance:** Relevant context regarding pre-payment accounts successfully fetched from prepayment.pdf
   - **Generated Answer Accuracy:** Satisfactory and precise.

4. **Query:** What are the provisions and guidelines regarding the acceptance of a proxy or authorized representatives for importers?
   - **Retrieved Context Relevance:** Accurate trade and proxy documentation retrieved from Acceptance-of-Importers-Proxy.pdf and ImportersProxy.pdf
   - **Generated Answer Accuracy:** Provided detailed step-by-step information based on the context.

5. **Query:** What are the guidelines and application details for residence visas in Sri Lanka?
   - **Retrieved Context Relevance:** Retrieved specific residence visa clauses from residence_visa.pdf
   - **Generated Answer Accuracy:** Correctly identified visa issuance procedures and rules.  

   ## Model Selection & Comparison

| Model Name | Provider | Strengths | Use Case in GovAssist SL |
| :--- | :--- | :--- | :--- |
| **llama-3.1-8b-instant** | Groq | Ultra-low latency, high speed, near-free token cost | **Intent Routing & Quick Classification** (Used by the Router Agent to instantly analyze user intent) |
| **llama-3.3-70b-versatile** | Groq | Advanced reasoning, excellent context handling, high accuracy | **Deep Reasoning & Response Synthesis** (Used by the Verifier Agent to generate final precise answers) |
| **mixtral-8x7b-32768** | Groq / OpenRouter | Large context window, strong multilingual support | **Document Context Processing** (Handling multi-page government PDFs effectively) |


```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Router as Router Agent (Llama-3.1-8B)
    participant Service as Service Agent (RAG Tool)
    participant Verifier as Verifier Agent (Llama-3.3-70B)

    User->>Router: Submits question / query
    Router->>Router: Analyzes intent and routes (Groq)
    Router->>Service: Forwards route context
    Service->>Service: Retrieves relevant chunks from Vector DB (Chroma)
    Service->>Verifier: Passes retrieved context & query
    Verifier->>Verifier: Synthesizes final response & extracts sources
    Verifier->>User: Displays AI response & sources

## Live App (Streamlit Cloud)
You can access the live application here: [GovAssist SL Live App](https://agentic-ai-assignment-9tf2osxrtpmkessyparbn6.streamlit.app)
