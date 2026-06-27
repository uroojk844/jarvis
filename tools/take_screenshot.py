from langchain.tools import tool
from pyautogui import screenshot


@tool
def take_screenshot() -> str:
    "Take the screenshot and return screenshot path"

    image = screenshot()
    file_name = "screen.png"

    image.save(file_name)

    # image.show("Screen.png")
    print("Took screenshot")

    return file_name
