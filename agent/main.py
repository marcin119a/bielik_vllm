import asyncio
import httpx
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, RunConfig, Runner
from agents.mcp import MCPServerStreamableHttp

from config import settings

mcp_helper_server = MCPServerStreamableHttp(
    name="My MCP Server",
    params={
        "url": "http://127.0.0.1:8001/mcp",
    },
)


class VLLMUnavailableError(RuntimeError):
    pass


async def ensure_vllm_available() -> None:
    models_url = f"{settings.vllm_base_url.rstrip('/')}/models"
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(5.0, connect=5.0)) as client:
            response = await client.get(models_url)
            response.raise_for_status()
    except httpx.HTTPError as exc:
        raise VLLMUnavailableError(
            f"vLLM endpoint {settings.vllm_base_url!r} is unreachable. "
            "Check VLLM_BASE_URL, network routing, and whether the server is listening on port 8000."
        ) from exc


async def main():
    openai_client = AsyncOpenAI(
        base_url=settings.vllm_base_url,
        api_key=settings.openai_api_key,
    )
    await ensure_vllm_available()
    async with mcp_helper_server:
        agent = Agent(
            name="Zegarmistrz światła purpurowy",
            instructions="Pomagasz z datą i czasem.",
            model=OpenAIChatCompletionsModel(
                model=settings.model_name,
                openai_client=openai_client,
            ),
            mcp_servers=[mcp_helper_server],
        )

        result = await Runner.run(
            agent,
            "Jaka jest dzisiejsza data?",
            run_config=RunConfig(tracing_disabled=True),
        )
        print(result.final_output)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except VLLMUnavailableError as exc:
        print(exc)
