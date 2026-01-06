from fastmcp import FastMCP

## This is my first MCP server sample:
app=FastMCP("my-MCP-server")

# Provide a simple calculator tool

@app.tool
def add(n1:int, n2:int)->int:
    """ Add 2 numbers and return the result. """
    return n1+n2

