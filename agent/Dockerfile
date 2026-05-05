FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

# Install without vllm/bitsandbytes — not needed for openai backend
RUN uv pip install --system \
    openai \
    openai-agents \
    fastapi \
    "uvicorn[standard]" \
    python-dotenv \
    mcp \
    httpx \
    pydantic \
    pydantic-settings \
    fastmcp

COPY config.py ./
COPY agent/ ./agent/

CMD ["python", "agent/main.py"]
