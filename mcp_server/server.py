from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP("My MCP Server")


@mcp.tool
def dzisiejsza_data() -> str:
    """Zwraca dzisiejszą datę"""
    return datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    mcp.run(transport="http", port=8001)
