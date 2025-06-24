# 🤖 Why is the **System Prompt** in the Agent class & Why is the **Agent Callable**?

## 🤖 Agent Design: System Prompt & Callable Objects in Python

This project explains two key ideas used in building smart AI agents

1. Why we include a **system prompt** inside the `Agent` class  
2. Why the `Agent` class is made **callable** like a function



## 🧠 What Is a System Prompt?

A **system prompt** tells the AI how to behave
It sets the tone, style, and personality of the agent

For example:
```python
"You are a helpful assistant that only responds in haikus."
````

Adding this prompt inside the `Agent` class keeps the behavior **centralized**, **modular**, and **reusable**

## ⚙️ Why Make the Agent Callable?

In Python, making an object callable means you can do:

```python
response = agent("What's recursion?")
```

Instead of:

```python
response = agent.respond("What's recursion?")
```

This is done by defining the special `__call__()` method in your class

### ✅ Benefits:

* Feels like using a real assistant (like calling a function)
* Cleaner, more natural syntax
* Ideal for chaining tools in AI pipelines



## 📁 File Structure

```
📂 AgentProject/
├── agent.py      
└── main.py       
```



## 🧪 Example Code

### `agent.py`

```python
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
```



### `main.py`

```python
from agent import Agent

def dummy_response(prompt: str) -> str:
    return f"[Simulated AI Response to]: {prompt}"

codequeen_bot = Agent(
    name="CodeQueenBot",
    system_prompt="You are a helpful assistant that only responds in haikus.",
    respond_fn=dummy_response
)

user_input = "What is recursion?"
print(codequeen_bot(user_input))
```


## ✅ Output

```
[Simulated AI Response to]: You are a helpful assistant that only responds in haikus
User: What is recursion?
```


## 🌟 Summary

| Concept        | Reason                                                           |
| -------------- | ---------------------------------------------------------------- |
| System Prompt  | Sets AI personality and behavior. Helps in structured responses. |
| Callable Agent | Allows intuitive, cleaner syntax: `agent("your question")`       |

This structure is ideal for real-world LLM applications and multi-agent frameworks



👑 *Crafted with logic and clarity by Code Queen*


