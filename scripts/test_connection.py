import json
from huggingface_hub import login
from tiny_agents import Agent

def main():
    with open("agents/playwright-agent.json") as f:
        config = json.load(f)

    agent = Agent.from_config(config)
    print("Agent loaded:", agent.name)

if __name__ == "__main__":
    main()
