from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from config import MODEL, TEMPERATURE
from tool_loader import load_tools
from utils import load_prompt

tools_list = load_tools()
tool_map = {tool.name: tool for tool in tools_list}

llm = ChatOllama(model=MODEL, temperature=TEMPERATURE)
llm_with_tools = llm.bind_tools(tools_list)

VISION_TOOLS = ["analyze_screen", "click", "double_click", "move_cursor"]

while True:
    question = input("You: ")
    # question = listen()

    if question.lower() in ["quit", "exit", "stop"]:
        break

    response = llm_with_tools.invoke(
        [SystemMessage(content=load_prompt("main")), HumanMessage(content=question)]
    )

    if response.tool_calls:
        print(response.tool_calls)

        responses = []
        # Execute only one visual tool
        if response.tool_calls[0]["name"] in VISION_TOOLS:
            tool_name = response.tool_calls[0]["name"]
            tool_args = response.tool_calls[0]["args"]

            tool_response = tool_map[tool_name].invoke(tool_args)
            responses.append(tool_response)

            # Execute all non-visual tools
        else:
            for tool in response.tool_calls:
                tool_name = tool["name"]
                tool_args = tool["args"]

                tool_response = tool_map[tool_name].invoke(tool_args)
                responses.append(tool_response)

        final_response = llm.invoke(
            [
                SystemMessage(content="""
                    You are an AI assistant.
                    Answer using the tool results only.
                    Keep responses short and natural.
                    Do not invent information.
                    """),
                HumanMessage(content=f"""
                    user question: {question},
                    Tool Result: {responses}
                    """),
            ]
        )
        # speak(final_response.content)
        print("Agent: ", final_response.content)
    else:
        print("Agent: ", response.content)
