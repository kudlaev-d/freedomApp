import os
import subprocess
import time

file = 'logs.txt'
log_path = os.path.join(os.path.dirname(__file__), file)

def has_logs() -> bool:
    return os.path.exists(log_path)

def log(message) -> None:
    with open(log_path, 'a') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def remove_logs() -> None:
    if has_logs():
        os.remove(log_path)

def open_dir() -> None:
    os.startfile(os.path.join(os.path.dirname(__file__)))

def open_log_file() -> None:
    subprocess.run(['notepad', log_path])