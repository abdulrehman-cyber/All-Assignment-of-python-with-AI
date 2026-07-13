import os
import time
from datetime import datetime, timedelta
import pygame


def set_alarm(alarm_time_str):
    try:
        alarm_time = datetime.strptime(alarm_time_str, "%H:%M:%S").time()
    except ValueError:
        raise ValueError("Please enter time in HH:MM:SS format.")

    now = datetime.now()
    alarm_datetime = datetime.combine(now.date(), alarm_time)
    if alarm_datetime <= now:
        alarm_datetime += timedelta(days=1)

    print(f"Alarm set for {alarm_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

    sound_file = "my_music.mp3"
    if not os.path.exists(sound_file):
        print(f"Warning: sound file '{sound_file}' not found. Alarm will still trigger visually.")

    try:
        pygame.mixer.init()
    except pygame.error as error:
        print(f"Warning: pygame mixer could not be initialized: {error}")
        return

    while True:
        now = datetime.now()
        if now >= alarm_datetime:
            print("WAKE UP!")
            if os.path.exists(sound_file):
                try:
                    pygame.mixer.music.load(sound_file)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(1)
                except pygame.error as error:
                    print(f"Unable to play sound: {error}")
            break

        remaining = alarm_datetime - now
        print(f"Time remaining: {str(remaining).split('.')[0]}", end=" ", flush=True)
        time.sleep(1)


if __name__ == "__main__":
    while True:
        alarm_time_input = input("Enter the alarm time (HH:MM:SS): ")
        try:
            set_alarm(alarm_time_input)
            break
        except ValueError as error:
            print(error)
