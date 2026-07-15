from datetime import datetime
import os

LOG_FOLDER = "logs"
LOG_FILE = os.path.join(LOG_FOLDER, "battery.log")


def log_event(message):

    os.makedirs(LOG_FOLDER, exist_ok=True)

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{current_time} - {message}\n")

    print(f"[LOG] {message}")