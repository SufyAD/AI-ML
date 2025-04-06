from langchain.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
ANTHROPIC_API_KEY=os.getenv('ANTHROPIC_API_KEY')

#create fastapi app
app = FastAPI(
    title="LangServe API routes",
    description="API routes for LangServe",
    version="1.0.0",
)

# define models
gemini_model = ChatGoogleGenerativeAI(
    api_key=GEMINI_API_KEY,
    model='gemini-1.5-flash' 
)

anthropic_model=ChatAnthropic(
    api_key=ANTHROPIC_API_KEY,
    model_name='claude-3-sonnet-20240229'
)

#create app_routes using langserve to create API end-points
gemini_prompt = ChatPromptTemplate.from_template("Can you write me an essay for high school level on {topic} within 100 lines?")
anthropic_prompt = ChatPromptTemplate.from_template("Can you write a beatiful heart-touching poem on {topic} within 4 lines")
add_routes(
    app,
    runnable=gemini_prompt|gemini_model,
    path='/essay'
)

add_routes(
    app,
    runnable=anthropic_prompt|anthropic_model,
    path='/poem'
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)