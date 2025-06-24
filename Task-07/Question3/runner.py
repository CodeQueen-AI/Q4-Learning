class Runner:
    @classmethod
    def run(cls, agent, user_prompt: str) -> str:
        """
        Run an agent with the given user prompt.
        This is a class method because we don’t need to create an instance of Runner.
        """
        print(f"Running agent '{agent.name}' with prompt: {user_prompt}")
        return agent(user_prompt)
