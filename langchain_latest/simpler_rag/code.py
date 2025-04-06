from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
import bs4 # beatiful soup 4 
import os 
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_vertexai import VertexAIEmbeddings

load_dotenv()

# Stage 1: Load from source
loader = TextLoader('notes.txt')
txt_doc1 = loader.load()
print(txt_doc1)


os.environ['GEMINI_API_KEY'] = os.getenv("GEMINI_API_KEY") #get and set key

# web loaders
# loader2 = WebBaseLoader(web_paths=('https://en.wikipedia.org/wiki/Ramadan',),
#                          bs_kwargs=dict(
#                              parse_only=bs4.SoupStrainer(
#                                  class_=("wikitable")
#                              )),)
# txt_doc2 = loader2.load()
# print(txt_doc2)

# Stage 2: Transform the loaded data
txt_splitter = RecursiveCharacterTextSplitter(chunk_size=50, chunk_overlap=10)
docs3 = txt_splitter.split_documents(txt_doc1)
for i in range(1,5):
    print('\n',docs3[:i])
    
# Stage 3: Embed the data/Store in Vector DB
embeddings = VertexAIEmbeddings(api_key="GEMINI_API_KEY", model="text-embedding-004")
embeddings.embed_query(docs3)


 

