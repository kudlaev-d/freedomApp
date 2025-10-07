import os
import threading
import time
import subprocess
from logs import log


running = False

# script_path: str = os.path.join(os.getcwd()) # Пропиши тут путь к файлу script_of_freedom на своем компе
script_path: str = "C:\\Users\\user\\PycharmProjects\\freedom\\script_of_freedom.py"

def run_script() -> None:
    counter: int = 0
    global running
    while running:
        subprocess.run(['python', script_path, 'script_of_freedom.py'])
        time.sleep(300)
        counter += 1
        log(f"Script worked {counter} times")

def start_script() -> None:
    global running
    if not running:
        running = True
        threading.Thread(target=run_script, daemon=True).start()
        log("Script was started")

def stop_script() -> None:
    global running
    running = False
    log("Script was stopped")

def run_script_one_time() -> None:
    subprocess.run(['python', script_path, 'script_of_freedom.py'])
    log(f"Script was started manually")


