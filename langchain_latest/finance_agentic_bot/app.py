import os
from dotenv import load_dotenv
import time
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_community.vectorstores import FAISS

load_dotenv()

### Important API keys for our lLM
api = os.getenv('GOOGLE_API_KEY')

# Streamlit UI setup
st.title("Agentic Finance Bot with Langchain Retrieval")
st.sidebar.title("Enter News Article URLs")

# Input URLs dynamically
urls = []
url_count = st.sidebar.number_input("Number of URLs", min_value=1, value=1)
for i in range(url_count):
    url = st.sidebar.text_input(f"URL {i+1}")
    if url:
        urls.append(url)

# Action button
process_urls = st.sidebar.button("Process URLs")

# Placeholder for status updates
main_placeholder = st.empty()

# Initialize LLM
llm = ChatGoogleGenerativeAI(api_key=api, model='gemini-1.5-flash')

# Main process
if process_urls and urls:
    try:
        # Step 1: Load documents from URLs
        main_placeholder.text("Loading data from URLs...")
        loader = UnstructuredURLLoader(urls=urls)
        documents = loader.load()

        # Step 2: Split documents into chunks
        main_placeholder.text("Splitting documents...")
        splitter = RecursiveCharacterTextSplitter(
            separators=['\n\n', '\n', '.', ','],
            chunk_size=1000,
            chunk_overlap=200
        )
        docs = splitter.split_documents(documents)

        # Step 3: Generate embeddings
        main_placeholder.text("Generating embeddings...")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_documents(docs, embeddings)

        # Step 4: Create retriever
        main_placeholder.text("Creating retriever from vector store...")
        retriever = vector_store.as_retriever()
        # After creating retriever
        st.session_state.retriever = retriever
        time.sleep(2)

        main_placeholder.success("Processing complete! ✅")
        time.sleep(2)

    except Exception as e:
        st.error(f"An error occurred: {e}")
    
    

# Input query
query = main_placeholder.text_input("Ask a question based on the articles:")
# creating a btn and spinner
is_submit = st.button("Submit")

if is_submit:
    if 'retriever' in st.session_state: 
        try:
            with st.spinner("Processing query..."):
                # Build QA chain using retriever
                chain = RetrievalQAWithSourcesChain.from_llm(
                    llm=llm, 
                    retriever=st.session_state.retriever # quick fix for retriever issue (to be used in the next state)
                    ) 
                result = chain({"question": query}, return_only_outputs=True)

            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("We Got You!")
            st.write(result['answer'])

            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                for src in sources.split("\n"):
                    st.write(f"- {src}")
            else:
                st.info("No sources found.")
                
        except Exception as e:
            st.error(f"An error occurred while processing: {e}")
    else:
        st.warning("Please process URLs first to initialize retriever.")
                