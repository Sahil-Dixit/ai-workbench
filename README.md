# AI Workbench

A multi-task LLM-powered text processing service built progressively across Module 0.

## Quick Start (Docker Compose)

```bash
cp .env.example .env
# Edit .env with your actual API key

docker compose up --build
```

- Backend API: http://localhost:8000
- Frontend UI: http://localhost:8501
- API Docs: http://localhost:8000/docs

## Manual Start (Development)

```bash
# Backend
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp ../.env.example .env  # Edit with your key
uvicorn app.main:app --reload

# Frontend (separate terminal)
cd frontend
pip install -r requirements.txt
BACKEND_URL=http://localhost:8000 streamlit run streamlit_app.py
```

## Deploy to EC2

```bash
# On a fresh EC2 instance:
chmod +x setup.sh
./setup.sh
```

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | /health | Service health check |
| POST | /summarize | Summarize text in bullet points |
| POST | /rewrite | Rewrite text professionally |
| POST | /keypoints | Extract key points |
| POST | /explain | Explain in simple terms |

## Architecture

```
Browser → Streamlit (8501) → FastAPI (8000) → LLM API (OpenAI)
```

## Agent Teaser

```bash
python agent_teaser.py
```

Demonstrates the think → act → observe loop using this API as a tool.