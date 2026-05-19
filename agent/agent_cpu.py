import asyncio
import psutil
from pydantic import BaseModel

from agents import Agent, Runner, function_tool, handoff


class Output(BaseModel):
    cpu_percent: float
    high_usage: bool
    recommendation: str


@function_tool
def check_cpu() -> dict:
    cpu = psutil.cpu_percent(interval=1)
    return {
        "cpu_percent": cpu,
        "high_usage": cpu > 80,
    }


cpu_agent = Agent(
    name="CPU Agent",
    instructions="""
    Sprawdź CPU narzędziem check_cpu.
    Zwróć wynik zgodny ze schematem Output.
    Jeśli high_usage=True, dodaj krótką rekomendację.
    """,
    tools=[check_cpu],
    output_type=Output,
)

main_agent = Agent(
    name="Main Agent",
    instructions="""
    Jeśli użytkownik pyta o CPU lub wydajność systemu,
    przekaż zadanie do CPU Agent.
    """,
    handoffs=[handoff(cpu_agent)],
)


async def main():
    result = await Runner.run(
        main_agent,
        "Sprawdź zużycie CPU",
    )

    output: Output = result.final_output
    print(output)


if __name__ == "__main__":
    asyncio.run(main())
