# Bielik Agent

Lokalny AI Agent oparty na polskim modelu językowym [Bielik](https://speakleash.org/), z MCP Serverem, streamingiem i FastAPI.

Projekt powstał na podstawie tutoriala: **https://grski.pl/bielik-cz-2**

## Stack

- **Model**: `speakleash/Bielik-4.5B-v3.0-Instruct` lub `Bielik-11B-v2.6-Instruct`
- **Serwowanie modelu**: vLLM z custom tool parserem z [`bielik-tools`](https://github.com/speakleash/bielik-tools)
- **Agent**: OpenAI Agents SDK (`openai-agents`)
- **MCP Server**: FastMCP (`fastmcp`)
- **API**: FastAPI + uvicorn
- **Konfiguracja**: pydantic-settings + `.env`

## Struktura projektu

```
.
├── agent/
│   └── main.py          # logika agenta (OpenAI Agents SDK + MCP)
├── api/                 # FastAPI endpoints ze streamingiem
├── mcp_server/
│   └── server.py        # własny MCP server (narzędzie: dzisiejsza_data)
├── bielik-tools/        # submoduł z custom tool parserem dla vLLM
├── config.py            # centralna konfiguracja przez pydantic-settings
├── pyproject.toml
└── .env.example
```

## Wymagania

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)
- Działający serwer vLLM z modelem Bielik

## Instalacja

```bash
uv sync
```

## Konfiguracja

Skopiuj `.env.example` do `.env` i uzupełnij wartości:

```bash
cp .env.example .env
```

```env
VLLM_BASE_URL=http://127.0.0.1:8000/v1
MODEL_NAME=speakleash/Bielik-4.5B-v3.0-Instruct
OPENAI_API_KEY=EMPTY
API_HOST=0.0.0.0
API_PORT=8080
```

`OPENAI_API_KEY=EMPTY` — vLLM nie wymaga klucza API, ale SDK wymaga niepustej wartości.

## Uruchomienie

### 1. MCP Server

```bash
uv run python -m mcp_server.server
```

Serwer startuje na `http://127.0.0.1:8001/mcp`.

### 2. Agent (tryb CLI)

```bash
uv run python -m agent.main
```

Agent łączy się z vLLM i MCP Serverem, zadaje przykładowe pytanie o datę i wypisuje odpowiedź.

## Źródła

- Tutorial: https://grski.pl/bielik-cz-2
- Modele Bielik: https://speakleash.org/
- bielik-tools (custom vLLM tool parser): https://github.com/speakleash/bielik-tools
