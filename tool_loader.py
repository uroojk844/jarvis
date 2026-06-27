import pkgutil
import importlib
from langchain_core.tools import BaseTool


def load_tools():
    tools = []

    package = "tools"

    for _, module_name, _ in pkgutil.iter_modules(["tools"]):
        module = importlib.import_module(
            f"{package}.{module_name}"
        )

        for obj in vars(module).values():
            if isinstance(obj, BaseTool):
                tools.append(obj)
                # print(obj.name)

    return tools