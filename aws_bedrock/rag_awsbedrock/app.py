# Step 2: Getting response from Claude/Llama LLMs in AWS bedrock
# Step 3: Convert this entire thing in an streamlit app

import boto3
from langchain_aws import BedrockEmbeddings
from langchain_aws import BedrockLLM
import streamlit as st
import json
import os
import sys

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.prompts import ChatPromptTemplate
from langchain.chains import RetrievalQA

# Bedrock Clients (configuration)
bedrock=boto3.client(service_name="bedrock-runtime")
# using AWS titan embeddings
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=bedrock)


# Step 1: Data ingestion using AWS Bedrock embeddings
def data_ingestion(): 
    loader = PyPDFDirectoryLoader("./data/")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    docs = text_splitter.split_text(documents)
    return docs

def get_vector_store(docs):
    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=bedrock_embeddings
    )
    # we can optionally persist
    # vector_db.save_local("faiss_index") # we'll locally save this file for future retrieval 
    # with ChromaDB
    vector_db.persist()

# Here are our both LLMs from AWS Bedrock
def get_claude_llm():
    llm = BedrockLLM(model_id="ai21.j2-mid-v1",
                     client=bedrock,
                     model_kwargs={'maxTokens':512})
    return llm

def get_llama_llm():
    llm=BedrockLLM(model_id="meta.llama2-70b-chat-v1",
                   client=bedrock,
                   model_kwargs={'max_gen_len':512})
    return llm
    

# Create our prompt for RAG
prompt = """
    Human: Use the following pieces of context to provide a 
    concise answer to the question at the end but usse atleast summarize with 
    100 words with detailed explaantions. If you don't know the answer, 
    just say that you don't know, don't try to make up an answer.

    <context>
    {context}
    </context

    Question: {question}

    Assistant:
"""

PROMPT = ChatPromptTemplate(template_format=prompt, input_variable=['context', 'question'])

# Now get the Rretrieved response from vector DB and sent to the augmented LLM for response generation
def get_llm_response(llm, vector_db, query):
    qa_chain = RetrievalQA.from_llm(
        llm, 
        chain_type="stuff",
        retriever=vector_db.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 3}
        ), 
        return_source_documents=True,
        prompt=PROMPT
    )
    resp = qa_chain({
        'query': query
    })
    return resp['result ']


# define the streamlit app
def main():
    st.title("LLM Augmented Retrieval")
    user_question = st.text_input("Ask a Question from the PDF Files")
    
    with st.sidebar:    
        st.title("Update Or Create Vector Store:")
        if st.button("Update Vectors"):
            with st.spinner("Processing..."):
                docs = data_ingestion()
                get_vector_store(docs)
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings) # load the vectors
                st.success("Done")
                
                
        
        if st.button("Claude Output"):
            with st.spinner("Processing..."):
                llm=get_claude_llm()
                #faiss_index = get_vector_store(docs)
                st.write(get_llm_response(llm,faiss_index,user_question))
                st.success("Done")
                
        if st.button("Claude Output"):
            with st.spinner("Processing..."):
                llm=get_claude_llm()
                #faiss_index = get_vector_store(docs)
                st.write(get_llm_response(llm,faiss_index,user_question))
                st.success("Done")
                
if __name__ == "__main__":
    main()
    
    
