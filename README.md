# Autonomous Multi-Agent AI Red-Teaming Harness

An automated, local-first adversarial red-teaming pipeline built with LangGraph, LangChain, and Ollama (Llama 3.2). The harness evaluates AI guardrails by pitting an attacking persona against a protected endpoint and scoring breach severity autonomously.

## Key Features
- Zero-Cost & Private: 100% local inference powered by Ollama (llama3.2).
- Cyclic Multi-Agent Loop: LangGraph state machine with dynamic defense rule accumulation.
- Structured Evaluation: Pydantic schemas for payload generation and severity scoring.
- Terminal UI: Rich audit reporting table displaying rounds, vectors, and pass/fail statuses.

## Quickstart
1. ollama pull llama3.2
2. source venv/bin/activate && pip install -r requirements.txt
3. python run.py
