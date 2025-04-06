# API Agent with Streamlit Chatbot

This project provides a FastAPI backend integrated with LangChain models and a Streamlit-based chatbot frontend.

## Getting Started

### Prerequisites
- Python 3.8+
- pip or poetry

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/api-agent.git
cd api-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

Or if using poetry:
```bash
poetry install
```

### Running the Applications

1. Start the FastAPI backend:
```bash
uvicorn app:app --reload
```

2. In a separate terminal, start the Streamlit chatbot:
```bash
streamlit run chatbot.py
```

### Usage

- Access the FastAPI backend at `http://localhost:8000`
- Access the Streamlit chatbot at `http://localhost:8501`

### Environment Variables

Create a `.env` file with the following variables:
```
GEMINI_API_KEY=your_gemini_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
```

## Project Structure

```
.
├── app.py            # FastAPI application
├── chatbot.py        # Streamlit chatbot
├── requirements.txt  # Python dependencies
├── pyproject.toml    # Poetry configuration
└── README.md         # This file
```

## License

MIT License
