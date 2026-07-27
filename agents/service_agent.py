class ServiceAgent:
    def __init__(self, retriever, groq_client):
        self.retriever = retriever
        self.client = groq_client

    def answer(self, query):
        docs = self.retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are GovAssist SL government assistant. Answer only using the given context accurately.

Context:
{context}

Question:
{query}

Answer:
"""
        
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",  
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        
        content = response.choices[0].message.content.strip()
        return content, docs