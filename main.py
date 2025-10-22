from langchain.agents import create_agent
from random import choice
from langchain_google_genai import ChatGoogleGenerativeAI  # noqa: F401
from langchain_openai import ChatOpenAI  # noqa: F401
from langchain_anthropic import ChatAnthropic  # noqa: F401
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage  # noqa: F401
from pydantic import SecretStr  # noqa: F401
import os  # noqa: F401



def dice_roll(sides: int = 6) -> int:
    """Simulates a dice roll."""
    choose_val = choice(range(1, sides + 1))
    print(f"Dice rolled: {choose_val}")
    return choose_val


def pow_number(base: int, exponent: int) -> int:
    """Calculates the power of a number."""
    result = base**exponent
    print(f"Calculating: {base}^{exponent} = {result}")
    return result


agent = create_agent(
    tools=[dice_roll, pow_number],
    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite-preview-09-2025"),
    system_prompt="あなたは、優秀で親切なアシスタントです。ユーザーがサイコロを振りたいときに、適切なツールを使ってサイコロの目を提供してください。",
)


resp = agent.invoke(
    input={
        "messages": [
            HumanMessage(
                content="6面体のサイコロを振って、出た目を2乗して教えてください。"
            )
        ]
    }
)

print(resp)
print(resp["messages"][-1].content)

agent.get_graph().print_ascii()