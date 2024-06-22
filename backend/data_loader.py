import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


def prepare_documents(df):
    documents = df['data'].tolist()
    metadatas = [{'role': role} for role in df['role']]
    ids = [f"doc{i}" for i in range(len(df))]
    return documents, metadatas, ids

def add_to_collection(collection, documents, metadatas, ids):
    collection.add(
        documents=documents,  
        metadatas=metadatas,  
        ids=ids  
    )
