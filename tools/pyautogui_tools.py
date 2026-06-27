from langchain.tools import tool
import pyautogui
from utils import highlight


@tool
def click(x, y) -> str:
    """
    Perform a single mouse click at the specified screen coordinates.

    Use after analyze_screen has identified the position.

    Only use coordinates returned by analyze_screen.

    Never invent coordinates.

    Examples:
    - click the login button
    - click the file
    - click the close button

    Never use for keyboard shortcuts.
    """

    pyautogui.click(x, y)
    highlight()

    return f"Clicked at {x},{y}"


@tool
def double_click(x: int, y: int) -> str:
    """
    Perform a double mouse click at the specified coordinates.

    Use to open files, folders, or applications identified on the screen.

    Examples:
    - open main.py
    - open a folder
    - launch a desktop icon

    Use after analyze_screen.
    """
    pyautogui.click(x, y)
    return f"Clicked at {x},{y}"


@tool
def move_cursor(x, y) -> str:
    """
    Move the mouse cursor to a screen position.

    Use before clicking if precise positioning is needed.

    Examples:
    - move to the login button
    - hover over a menu
    - position the cursor

    Does not perform a click.
    """

    pyautogui.moveTo(x, y)
    highlight()

    return f"Moved to {x},{y}"


@tool
def press(key) -> str:
    """
    Press a single keyboard key.

    Examples:
    - enter
    - escape
    - tab
    - backspace
    - space

    Use only for a single key.

    For keyboard shortcuts use the hotkey tool.
    """
    pyautogui.press(key)
    return f"Pressed {key}"


@tool
def hotkey(key: list[str]) -> str:
    """
    Press keyboard shortcuts.

    Examples:
    - ['win', 'd'] show desktop
    - ['win', 'm'] minimize windows
    - ['ctrl', 's'] save
    - ['ctrl', 'c'] copy
    - ['ctrl', 'v'] paste
    - ['alt', 'tab'] switch windows
    - ['alt', 'f4'] close window

    Use whenever the user mentions:
    - shortcut
    - hotkey
    - press ctrl
    - press alt
    - press win

    Never use click for keyboard shortcuts.
    """

    pyautogui.hotkey(*key)
    return f"Pressed {' + '.join(key)}"


@tool
def write(message: str) -> str:
    """
    Type text using the keyboard.

    Examples:
    - type hello world
    - enter a username
    - write the password
    - search for vscode

    Use only for text input.

    Do not use for keyboard shortcuts.
    """
    pyautogui.write(message)
    return f"Wrote {message}"
