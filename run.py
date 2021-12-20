from subprocess import run
from time import sleep

file_path = "main.py"
restart_timer = 2

def start_script():
    print("start_script")
    try:
        run("python "+file_path, check=True)
    except:
        handle_crash()

def handle_crash():
    print("handle_crash")
    sleep(restart_timer)
    start_script()

start_script()