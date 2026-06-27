from langchain.tools import tool
import ollama
from config import IMAGE_MODEL
from tools import take_screenshot
from utils import load_prompt
import os
from PIL import Image

@tool
def analyze_screen(task:str) -> str:
    """
    Analyze the current screen.

    The task argument is REQUIRED.

    Examples:
    task="find main.py"
    task="find the login button"
    task="locate the close button"
    task="identify the active window"

    Never leave task empty.
    """

    take_screenshot.take_screenshot.run({})

    print(f"Analyzing {task}")

    Image.open("screen.png").show()

    agent = ollama.generate(
        model=IMAGE_MODEL,
        prompt=task,
        system=load_prompt("vision"),
        images=["screen.png"],
    )

    raw = agent.response.strip() if agent.response is not None else ""
    print("Image Response: ", raw)

    return raw
