import tkinter as tk
from typing import Literal

from logic import stop_script, start_script, run_script_one_time
from logs import remove_logs, open_dir, has_logs, open_log_file

root = tk.Tk()

root['bg'] = '#fafafa'
root.title('Freedom app')
root.wm_attributes('-alpha', 1)
root.geometry('300x300')

root.resizable(width=False, height=False)

def click_start_script() -> None:
    start_button.config(text="In progress...", state="disabled")
    stop_button.config(state="normal")
    remove_logs_button.config(state="normal")
    open_logs_button.config(state="normal")
    start_script()

def click_stop_button() -> None:
    start_button.config(text="Start", state="normal")
    stop_button.config(state="disabled")
    stop_script()

def click_remove_logs_button() -> None:
    remove_logs()
    remove_logs_button.config(state="disabled")
    open_logs_button.config(state="disabled")

def click_open_logs() -> None:
    open_log_file()

def get_remove_logs_button_state() -> Literal["normal", "disabled"]:
    return "normal" if has_logs() else "disabled"

start_button = tk.Button(root, text='Start', command=click_start_script, width=15, height=2)
stop_button = tk.Button(root, text='Stop', command=click_stop_button, width=15, height=2, state="disabled")
open_logs_button = tk.Button(root, text='Open logs', command=click_open_logs, width=15, height=2,
                               state=get_remove_logs_button_state())
remove_logs_button = tk.Button(root, text='Remove logs', command=click_remove_logs_button, width=15, height=2,
                               state=get_remove_logs_button_state())
open_dir_button = tk.Button(root, text='Open directory', command=open_dir, width=15, height=2)
manual_start_button = tk.Button(root, text='Manual start', command=run_script_one_time, width=15, height=2)

start_button.pack(pady=5)
stop_button.pack(pady=5)
open_logs_button.pack(pady=5)
remove_logs_button.pack(pady=5)
open_dir_button.pack(pady=5)
manual_start_button.pack(pady=5)

root.mainloop()