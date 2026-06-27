from pathlib import Path
from typing import Optional
import os
from langchain.tools import tool


def get_drives():
    """Return available Windows drives."""
    drives = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        drive = f"{letter}:\\"
        if os.path.exists(drive):
            drives.append(drive)
    return drives


@tool
def search_files(
    filename: str,
    extension: Optional[str] = None,
    max_results: int = 10,
):
    """
    Search the computer for files.

    Args:
        filename: Partial or full filename.
        extension: Optional extension like '.pdf', '.txt', '.py'
        max_results: Maximum number of results.

    Returns:
        List of matching files.
    """

    filename = filename.lower()

    if extension:
        extension = extension.lower()
        if not extension.startswith("."):
            extension = "." + extension

    results = []

    for drive in get_drives():

        for root, dirs, files in os.walk(
            drive,
            topdown=True,
            onerror=lambda e: None,
        ):

            # Skip inaccessible/system folders
            dirs[:] = [
                d
                for d in dirs
                if d.lower()
                not in (
                    "$recycle.bin",
                    "system volume information",
                )
            ]

            for file in files:

                name = file.lower()

                if filename not in name:
                    continue

                if extension and not name.endswith(extension):
                    continue

                full_path = str(Path(root) / file)

                results.append(
                    {
                        "name": file,
                        "path": full_path,
                    }
                )

                if len(results) >= max_results:
                    return results

    return results

