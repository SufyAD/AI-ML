from langchain_google_vertexai import VertexAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
api_key = os.getenv("GEMINI_API_KEY")  # Get the GEMINI_API_KEY from environment variables

# Stage 3: Embed the data/Store in Vector DB
embeddings = VertexAIEmbeddings(model="text-embedding-004")
embeddings.embed_query("Hello, world!")