from agent import Agent
from runner import Runner

# Dummy LLM response simulator
def dummy_response(prompt: str) -> str:
    return f"[AI Reply]: {prompt}"

# Define an Agent
codequeen_agent = Agent(
    name="CodeQueenBot",
    system_prompt="You are a motivational AI assistant.",
    respond_fn=dummy_response
)

# Run the agent using Runner (no instance needed!)
output = Runner.run(codequeen_agent, "How can I learn fast?")
print(output)
