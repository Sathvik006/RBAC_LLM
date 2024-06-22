import chromadb

def create_http_client():
    return chromadb.HttpClient()

def get_or_create_collection(client, collection_name):
    return client.get_or_create_collection(collection_name)
