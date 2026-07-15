import os
import winsound

SOUND_FILE = os.path.join("assets", "sounds", "alert.wav")


def play_alert():
    if os.path.exists(SOUND_FILE):
        winsound.PlaySound(
            SOUND_FILE,
            winsound.SND_FILENAME | winsound.SND_ASYNC
        )