class RouterAgent:
    def __init__(self, groq_client):
        self.client = groq_client

    def route(self, query):
        
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "Classify the user query into categories like: passport, driving_license, civil_registration, or general."},
                {"role": "user", "content": query}
            ],
            temperature=0.1
        )
        return response.choices[0].message.content.strip()