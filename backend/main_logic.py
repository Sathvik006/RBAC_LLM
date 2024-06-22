
from data_loader import load_data, prepare_documents, add_to_collection
from embedding_model import text_embedding
from db_client import create_http_client, get_or_create_collection
from query_model import query_model, get_prompt

COLLECTION_NAME = "RoleBase_collection2"
collection = None

def initialize_collection():
    global collection
    client = create_http_client()
    collection = get_or_create_collection(client, COLLECTION_NAME)

def load_and_add_data(file_path):
    df = load_data(file_path)
    documents, metadatas, ids = prepare_documents(df)
    add_to_collection(collection, documents, metadatas, ids)

def generate_context(user, query):
    vector = text_embedding(query).tolist()
    results = collection.query(
        query_embeddings=vector,
        n_results=2,
        where={"role": user}
    )
    res = "\n".join(str(item) for item in results['documents'][0])
    return res

def generate_response(context, query):
    prompt = get_prompt(context, query)
    payload = {"inputs": prompt}
    response = query_model(payload)
    response_text = response[0]['generated_text'].split("Response:")[1].strip()
    return response_text

initialize_collection()
