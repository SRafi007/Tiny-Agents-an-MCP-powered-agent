import json
from tiny_agents import Agent

def main():
    with open("agents/playwright-agent.json") as f:
        config = json.load(f)

    agent = Agent.from_config(config)

    response = agent.run("Open Brave search, look up HF inference providers and summarize.")
    print(response)

if __name__ == "__main__":
    main()
