from langchain.tools import tool
import subprocess


def is_safe(command: str):
    cmd = command.lower()

    for blocked in BLOCKED:
        if blocked in cmd:
            return False

    return True


@tool
def execute_cmd(command: str) -> str:
    """
    Execute safe Windows CMD commands.

    Use for:
    - opening applications
    - opening folders
    - creating folders
    - launching programs

    Examples:
    - start notepad
    - start chrome
    - mkdir Test
    - explorer D:\\

    Do not use for keyboard shortcuts.
    Do not invent file paths.
    """

    try:
        if not is_safe(command):
            return "Command blocked for safety."

        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=10
        )

        if result.returncode == 0:
            return result.stdout.strip()

        return result.stderr.strip()

    except Exception as e:
        return str(e)


BLOCKED = [
    "del",
    "erase",
    "format",
    "shutdown",
    "restart",
    "taskkill",
    "rd",
    "rmdir",
    "diskpart",
    "reg delete",
    "sc delete",
    "net user",
    "powershell",
    "curl",
    "wget",
]
