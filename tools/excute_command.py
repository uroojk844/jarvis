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
    Execute Windows CMD or PowerShell commands.

    Examples:
    - Open a file:
        start "" "C:\\Movies\\movie.mkv"

    - Open a folder:
        explorer "C:\\Users\\Urooj\\Downloads"

    - Open Chrome:
        start chrome

    - Launch Notepad:
        start notepad

    - Open a URL:
        start https://youtube.com

    Use this tool whenever the user's goal is to launch, open, play, or execute something.
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
