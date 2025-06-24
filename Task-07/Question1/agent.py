from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    role: str
    instructions: str

    def introduce(self):
        return f"I am {self.name}, my role is {self.role}. Instructions: {self.instructions}"
