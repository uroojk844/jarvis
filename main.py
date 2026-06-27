from langchain_ollama import ChatOllama
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    AIMessage,
    ToolMessage,
)

from config import MODEL, TEMPERATURE
from tool_loader import load_tools
from utils import load_prompt

tools_list = load_tools()
tool_map = {tool.name: tool for tool in tools_list}

llm = ChatOllama(
    model=MODEL,
    temperature=TEMPERATURE,
)

llm_with_tools = llm.bind_tools(tools_list)

while True:

    question = input("You: ")

    if question.lower() in ["exit", "quit"]:
        break

    messages = [
        SystemMessage(content=load_prompt("main")),
        HumanMessage(content=question),
    ]

    while True:

        response = llm_with_tools.invoke(messages)

        messages.append(response)

        if not response.tool_calls:
            print("Agent:", response.content)
            break

        print(response.tool_calls)

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(f"\nRunning {tool_name}...")

            tool_result = tool_map[tool_name].invoke(tool_args)

            print(tool_result)

            messages.append(
                ToolMessage(
                    content=str(tool_result),
                    tool_call_id=tool_call["id"],
                )
            )