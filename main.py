import time

from config import POLL_INTERVAL, DEBOUNCE_TIME
from battery import get_battery
from notifier import show_notification
from logger import log_event

previous_state = None

print("Battery Monitor Started...")
print("Press Ctrl + C to stop.\n")

while True:

    battery = get_battery()

    if battery is None:
        print("No battery detected.")
        break

    charging = battery.power_plugged

    if previous_state is None:
        previous_state = charging

    elif charging != previous_state:

        if charging:

            print("🔌 Charging Started")

            show_notification(
                "Charging Started",
                "Your laptop is charging again."
            )

            log_event("Charging Started")

        else:

            print("Checking if charging really stopped...")

            time.sleep(DEBOUNCE_TIME)

            battery = get_battery()

            if battery is not None and not battery.power_plugged:

                print("⚠ Charging Stopped")

                show_notification(
                    "Charging Stopped",
                    "Your laptop is no longer charging!"
                )

                log_event("Charging Stopped")

            else:

                print("False alarm ignored.")

        # Update the previous state with the latest battery status
        battery = get_battery()

        if battery is not None:
            previous_state = battery.power_plugged

    time.sleep(POLL_INTERVAL)