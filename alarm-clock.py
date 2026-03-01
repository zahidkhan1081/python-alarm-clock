import pygame as pg
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR + CLEAR_AND_RETURN, end="")

    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Time left: {minutes_left:02d}:{seconds_left:02d}")

    print(f"{CLEAR_AND_RETURN}⏰ Time's up!")

    pg.mixer.init()
    pg.mixer.music.load("alarm-sound.wav")
    pg.mixer.music.play(1)   # loop forever

    input("Press Enter to stop the alarm...")
    pg.mixer.music.stop()
    
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

total_seconds = minutes * 60 + seconds
alarm(total_seconds)