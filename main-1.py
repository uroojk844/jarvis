from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from config import MODEL, TEMPERATURE, MAIN_SYSTEM_PROMPT
from tool_loader import load_tools
from utils import listen, speak

tools_list = load_tools()
tool_map = {tool.name: tool for tool in tools_list}

llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)
llm_with_tools = llm.bind_tools(tools_list)


while True:
    question = input("You: ")

    if question.lower() in ["quit", "exit"]:
        break

    messages = [
        SystemMessage(content=MAIN_SYSTEM_PROMPT),
        HumanMessage(content=question),
    ]

    while True:
        response = llm_with_tools.invoke(messages)

        if not response.tool_calls:
            print(response.content)
            break

        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        result = tool_map[tool_name].invoke(tool_args)

        messages.append(response)

        messages.append(HumanMessage(content=f"""
            Tool {tool_name} returned:

            {result}
            """))
