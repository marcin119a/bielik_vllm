FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY mcp_server/ ./mcp_server/

RUN uv pip install --system fastmcp

EXPOSE 8001

CMD ["python", "mcp_server/server.py"]
