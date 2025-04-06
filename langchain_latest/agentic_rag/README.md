# 🔍 Multi-Source RAG Agent

A Retrieval-Augmented Generation (RAG) application built using **LangChain's Agent framework** and powered by **multiple retrieval tools**. This agent can automatically route user queries to the most relevant data source using OpenAI's function calling logic.

## 💡 What is it?

This project implements a **multi-source agentic RAG system** that integrates:
- ✅ Web scraping via **WebLoader**
- 📚 **Wikipedia** search via API
- 🧠 **ArXiv research papers** retrieval tool

The core intelligence is driven by the `create_openai_tools_agent` from LangChain, which:
- Parses your query
- Decides the most appropriate tool (source)
- Retrieves the contextual information
- Generates an answer using the LLM (OpenAI)

No manual routing — everything is handled *agentically* ✨

## 🛠️ Tools Used

| Source | Description |
|--------|-------------|
| `WebLoader` | Scrapes content from public web pages |
| `WikipediaSearchTool` | Performs semantic search over Wikipedia topics |
| `ArxivTool` | Retrieves summaries of research papers from Arxiv.org |

## 📦 Tech Stack

- LangChain (Agents, Tools, RAG)
- Gemini (GPT-4)
- Python
- Arxiv API / Wikipedia API
- VectorStore (e.g., FAISS or Chroma)

## 🧠 Agentic RAG in Action

Check out this diagram for a peek behind the scenes:  
*(Attach your chosen diagram here)*