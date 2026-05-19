import asyncio
import psutil

from agents import Agent, Runner, function_tool, handoff


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
    Jeśli high_usage=True, ostrzeż użytkownika i podaj krótką rekomendację.
    """,
    tools=[check_cpu],
)

main_agent = Agent(
    name="Main Agent",
    instructions="""
    Jesteś głównym agentem.
    Jeśli użytkownik pyta o CPU lub wydajność systemu,
    przekaż zadanie do CPU Agent.
    """,
    handoffs=[
        handoff(cpu_agent),
    ],
)


async def main():
    result = await Runner.run(
        main_agent,
        "Sprawdź zużycie CPU",
    )
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
