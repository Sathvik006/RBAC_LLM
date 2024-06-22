from sentence_transformers import SentenceTransformer

def text_embedding(query):
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    return model.encode(query)
