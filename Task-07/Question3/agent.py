from dataclasses import dataclass
from typing import Callable

@dataclass
class Agent:
    name: str
    system_prompt: str
    respond_fn: Callable[[str], str]

    def __call__(self, user_input: str) -> str:
        prompt = f"{self.system_prompt}\nUser: {user_input}"
        return self.respond_fn(prompt)
