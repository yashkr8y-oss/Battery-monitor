import os
import winsound

SOUND_FILE = os.path.join("assets", "sounds", "alert.wav")


def play_alert():
    print("Looking for:", SOUND_FILE)
    print("Exists:", os.path.exists(SOUND_FILE))

    if os.path.exists(SOUND_FILE):
        print("Playing sound...")
        winsound.PlaySound(
            SOUND_FILE,
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )
    else:
        print("Alert sound not found.")