from itertools import cycle
import threading
import time
import sys


class Spinner:
    def __init__(self, text="Working"):
        self.text = text
        self.running = False
        self.frames = cycle(["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"])

    def _animate(self):
        while self.running:
            sys.stdout.write(f"\r{next(self.frames)} {self.text}")
            sys.stdout.flush()
            time.sleep(0.08)

    def start(self):
        self.running = True
        self.thread = threading.Thread(target=self._animate)
        self.thread.daemon = True
        self.thread.start()

    def stop(self, message="Done"):
        self.running = False
        self.thread.join()
        print(f"\r✔ {message}{' ' * 20}")