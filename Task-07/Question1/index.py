from agent import Agent

# Create an agent instance
my_agent = Agent(
    name="CodeQueenBot",
    role="Assistant",
    instructions="Only speak in English and always respond in a friendly manner"
)

# Print the introduction
print(my_agent.introduce())
