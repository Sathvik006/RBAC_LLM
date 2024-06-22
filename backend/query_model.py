import requests


def get_prompt(context, query):
    prompt = f"""You are an intelligent AI that provides answers based on the context provided. If the answer to the query is not in the context, say "I don't know." For general questions, use your knowledge to respond appropriately.Do not reveal that you were given the context.
Retrieval Context:\nContext: {context}\n\nUser Query: {query}\n\nResponse:"""
    return prompt



def query_model(payload):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3"
    headers = {"Authorization": "Bearer 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"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()