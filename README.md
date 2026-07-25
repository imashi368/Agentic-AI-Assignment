## Retrieval Evaluation

I tested my RAG pipeline with 5 sample queries to evaluate the relevance and accuracy of the retrieved context and generated responses:

1. **Query:** What are the required application steps and supporting documents needed to open a pre-payment account in ASYCUDA?
   - **Retrieved Context Relevance:** High. Retrieved correct chunks from customs/ASYCUDA documentation.
   - **Generated Answer Accuracy:** Accurate and aligned with official guidelines.

2. **Query:** What are the conditions and regulations applicable for the Widows' and Orphans' Pension Scheme?
   - **Retrieved Context Relevance:** High. Extracted exact pension scheme regulations.
   - **Generated Answer Accuracy:** Clear and well-synthesized by the agent.

3. **Query:** What are the specific guidelines mentioned for registering proxy documents or handling authorized representatives?
   - **Retrieved Context Relevance:** Relevant context successfully fetched.
   - **Generated Answer Accuracy:** Satisfactory.

4. **Query:** What are the regulations and control lists regarding import and export processing?
   - **Retrieved Context Relevance:** Accurate trade control documentation retrieved.
   - **Generated Answer Accuracy:** Provided detailed information based on context.

5. **Query:** What is the procedure and what are the forms required for accident leave under Paragraph 9:1:4 of E-Code Chapter XII?
   - **Retrieved Context Relevance:** Retrieved specific E-Code paragraphs.
   - **Generated Answer Accuracy:** Correctly identified leave procedures.

   ## Model Selection & Comparison

| Model Name | Provider | Strengths | Use Case in GovAssist SL |
| :--- | :--- | :--- | :--- |
| **google/flan-t5-small** | Hugging Face | Lightweight, fast, runs locally without API keys | Primary local model for text generation & synthesis |
| **Llama 3 (8B)** | Groq / OpenRouter | High speed, excellent reasoning capabilities | Alternative cloud model for complex query handling |
| **Mistral 7B** | OpenRouter | Strong multilingual and structured output support | Suitable for processing multi-lingual government documents |

```mermaid
sequenceDiagram
    autonumber
    actor User
    participant Router as Router Agent
    participant Service as Service Agent (RAG Tool)
    participant Verifier as Verifier Agent

    User->>Router: Submits question / query
    Router->>Router: Analyzes intent and routes
    Router->>Service: Forwards route context
    Service->>Service: Retrieves relevant chunks from Vector DB
    Service->>Verifier: Passes retrieved context & query
    Verifier->>Verifier: Synthesizes final response
    Verifier->>User: Displays AI response & sources
