import pandas as pd
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
import os

QDRANT_URL = "https://22a8f781-2788-4605-b1eb-8b0f85a0ea9b.europe-west3-0.gcp.cloud.qdrant.io:6333"
QDRANT_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.6M5lZ6gLYq-yYb8qo1XngO_6BZKUnqwDeRaN8bCcABY"
COLLECTION_NAME = "optimalsense_rag"
CSV_PATH = os.path.join("data", "symptom2disease", "Symptom2Disease.csv")

def main():
    print(f"Reading {CSV_PATH} ...")
    df = pd.read_csv(CSV_PATH)
    # Each row as a string: "Symptom: ..., Disease: ..., ..."
    texts = df.astype(str).apply(lambda x: ', '.join(f'{col}: {val}' for col, val in x.items()), axis=1).tolist()
    print(f"Loaded {len(texts)} rows from CSV.")

    print("Embedding rows...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts, show_progress_bar=True)
    vector_size = embeddings.shape[1]

    print(f"Connecting to Qdrant Cloud at {QDRANT_URL} ...")
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY, timeout=60)
    print(f"Recreating collection '{COLLECTION_NAME}' with vector size {vector_size} ...")
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config={"size": vector_size, "distance": "Cosine"}
    )
    print(f"Uploading {len(texts)} vectors to Qdrant ...")
    points = [
        {"id": i, "vector": emb.tolist(), "payload": {"text": txt}}
        for i, (emb, txt) in enumerate(zip(embeddings, texts))
    ]
    client.upload_points(
        collection_name=COLLECTION_NAME,
        points=points,
        batch_size=256,
        parallel=4
    )
    print("🎉 Successfully uploaded Symptom2Disease data to Qdrant Cloud!")

if __name__ == "__main__":
    main() 