import json
from tiny_agents import Agent

def main():
    with open("agents/playwright-agent.json") as f:
        config = json.load(f)

    agent = Agent.from_config(config)
    tools = agent.list_tools()

    print("Available tools in this agent:")
    for t in tools:
        print(" -", t["name"])

if __name__ == "__main__":
    main()
