from agent import Agent

# Define a simple dummy LLM response simulator
def dummy_response(prompt: str) -> str:
    return f"[Simulated AI Response to]: {prompt}"

# Create an Agent with a system prompt
codequeen_bot = Agent(
    name="CodeQueenBot",
    system_prompt="You are a helpful assistant that only responds in haikus.",
    respond_fn=dummy_response
)

# Use the agent like a function!
user_question = "What is recursion?"
response = codequeen_bot(user_question)

print(response)
