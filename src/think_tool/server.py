#!/usr/bin/env python3

from typing import Any, Dict, List, Optional
import json
import datetime
from mcp.server.fastmcp import FastMCP

class ThinkToolServer:
    def __init__(self, server_name="think-tool"):
        # Initialize FastMCP server
        self.mcp = FastMCP(server_name)
        
        # Store the thoughts for logging purposes
        self.thoughts_log = []
        
        # Register tools
        self.register_tools()
    
    def register_tools(self):
        # Register the think tool
        @self.mcp.tool()
        async def think(thought: str="") -> str:
            """Use this tool to think about something. It will not obtain new information or change anything, 
            but just append the thought to the log. Use it when complex reasoning or cache memory is needed.

            Args:
                thought: A thought to think about. This can be structured reasoning, step-by-step analysis,
                        policy verification, or any other mental process that helps with problem-solving.
            """
            # Log the thought with a timestamp
            timestamp = datetime.datetime.now().isoformat()
            self.thoughts_log.append({
                "timestamp": timestamp,
                "thought": thought
            })
            
            # Return a confirmation
            return f"Thought recorded: {thought[:50]}..." if len(thought) > 50 else f"Thought recorded: {thought}"

        @self.mcp.tool()
        async def get_thoughts() -> str:
            """Retrieve all thoughts recorded in the current session.
            
            This tool helps review the thinking process that has occurred so far.
            """
            if not self.thoughts_log:
                return "No thoughts have been recorded yet."
            
            formatted_thoughts = []
            for i, entry in enumerate(self.thoughts_log, 1):
                formatted_thoughts.append(f"Thought #{i} ({entry['timestamp']}):\n{entry['thought']}\n")
            
            return "\n".join(formatted_thoughts)

        @self.mcp.tool()
        async def clear_thoughts() -> str:
            """Clear all recorded thoughts from the current session.
            
            Use this to start fresh if the thinking process needs to be reset.
            """
            count = len(self.thoughts_log)
            self.thoughts_log = []
            return f"Cleared {count} recorded thoughts."

        @self.mcp.tool()
        async def get_thought_stats() -> str:
            """Get statistics about the thoughts recorded in the current session."""
            if not self.thoughts_log:
                return "No thoughts have been recorded yet."
            
            total_thoughts = len(self.thoughts_log)
            avg_length = sum(len(entry["thought"]) for entry in self.thoughts_log) / total_thoughts if total_thoughts else 0
            longest_thought = max((len(entry["thought"]), i) for i, entry in enumerate(self.thoughts_log)) if self.thoughts_log else (0, -1)
            
            stats = {
                "total_thoughts": total_thoughts,
                "average_length": round(avg_length, 2),
                "longest_thought_index": longest_thought[1] + 1 if longest_thought[1] >= 0 else None,
                "longest_thought_length": longest_thought[0] if longest_thought[0] > 0 else None
            }
            
            return json.dumps(stats, indent=2)
    
    def run(self, transport='stdio'):
        """Run the server with the specified transport"""
        print(f"Starting Think Tool MCP Server with {transport} transport...")
        self.mcp.run(transport=transport)


def main():
    server = ThinkToolServer()
    server.run()


if __name__ == "__main__":
    main()