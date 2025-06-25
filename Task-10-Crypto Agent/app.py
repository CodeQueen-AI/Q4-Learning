import chainlit as cl
from crypto_agent import CryptoDataAgent

agent = CryptoDataAgent()

@cl.on_message
async def main(message: cl.Message):
    symbol = message.content.strip()
    price = agent.get_price(symbol)

    if price:
        await cl.Message(content=f"💰 The current price of {symbol.upper()} is **${price}**").send()
    else:
        await cl.Message(content="❌ Invalid symbol or data not found. Try BTC, ETH, etc.").send()
