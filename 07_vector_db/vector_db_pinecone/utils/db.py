# Import the Pinecone library
from pinecone import Pinecone
from test_db import records
import time
from dotenv import load_dotenv
import os

load_dotenv()  
api_key = os.getenv("PINECONE_API_KEY") 

# Initialize a Pinecone client with your API key
pc = Pinecone(api_key=api_key)

# Create a dense index with integrated embedding
index_name = "langhcain-rag-index"
if not pc.has_index(index_name):
    pc.create_index_for_model(
        name=index_name,
        cloud="aws",
        region="us-east-1",
        embed={
            "model":"llama-text-embed-v2",
            "field_map":{"text": "chunk_text"}
        }
    )
    
# Target the index
dense_index = pc.Index(index_name)

# Upsert the records into a namespace
dense_index.upsert_records("langchain-rag", records)

# Wait for the upserted vectors to be indexed
time.sleep(10)

# View stats for the index
stats = dense_index.describe_index_stats()
print(stats)

# Define the query
query = "The Eiffel Tower was completed in 1889 "

# Search the dense index
results = dense_index.search(
    namespace="langchain-rag",
    query={
        "top_k": 10,
        "inputs": {
            'text': query
        }
    }
)

# Print the results
for hit in results['result']['hits']:
        print(f"id: {hit['_id']:<5} | score: {round(hit['_score'], 2):<5} | category: {hit['fields']['category']:<10} | text: {hit['fields']['chunk_text']:<50}")

# Delete the index
pc.delete_index(index_name)