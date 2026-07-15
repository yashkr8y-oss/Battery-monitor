import time
import psutil
from winotify import Notification

previous_state = None

print("Battery Monitor Started...")
print("Press Ctrl + C to stop.\n")

while True:

    battery = psutil.sensors_battery()

    if battery is None:
        print("No battery detected.")
        break

    charging = battery.power_plugged

    if previous_state is None:
        previous_state = charging

    elif charging != previous_state:

        if charging:
            print("🔌 Charging Started")

            toast = Notification(
                app_id="Battery Monitor",
                title="Charging Started",
                msg="Your laptop is charging again."
            )
            toast.show()

        else:
            print("⚠ Charging Stopped")

            toast = Notification(
                app_id="Battery Monitor",
                title="Charging Stopped",
                msg="Your laptop is no longer charging!"
            )
            toast.show()

        previous_state = charging

    time.sleep(2)