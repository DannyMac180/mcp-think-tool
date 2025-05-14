[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/dannymac180-mcp-think-tool-badge.png)](https://mseep.ai/app/dannymac180-mcp-think-tool)

# MCP Think Tool Server

A Model Context Protocol (MCP) server implementing the "think" tool for improving Claude's complex reasoning capabilities.

## Overview

This MCP server implements the "think" tool as described in Anthropic's [blog post](https://www.anthropic.com/engineering/claude-think-tool), which provides Claude with a dedicated space for structured thinking during complex problem-solving tasks. The think tool has been shown to significantly improve performance in complex tasks requiring policy adherence and reasoning in long chains of tool calls.

## Features

- **Structured Thinking Space**: Provides Claude with a dedicated place to break down complex problems
- **Thought History**: Maintains a log of all thoughts with timestamps for reference
- **Statistics and Analysis**: Offers metadata about thinking patterns
- **Clean Slate Option**: Allows clearing thought history when starting fresh

## Installation

Install from PyPI:

```bash
pip install mcp-think-tool
```

## Configuration

### Windsurf
To use this tool with Claude in Windsurf, add the following configuration to your MCP config file:

```json
"think": {
    "command": "/home/xxx/.local/bin/mcp-think-tool",
    "args": [],
    "type": "stdio",
    "pollingInterval": 30000,
    "startupTimeout": 30000,
    "restartOnFailure": true
}
```

The `command` field should point to the directory where you installed the python package using pip.

### Docker

You can install this MCP server with only the Dockerfile

First download the Dockerfile, navigate to its directory, and build the Docker image

````
docker build -t mcp-think-tool .
````

Then add the following configuration your MCP config file

````json
"think": {
    "command": "docker",
    "args": ["run", "--rm", "-i", "mcp-think-tool"]
}
````

This was tested and working with **Claude Desktop** and **Cursor**