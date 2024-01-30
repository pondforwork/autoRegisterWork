import time
import pyautogui as pg

import keyboard

def type_thai(text):
    keyboard.write(text)
    time.sleep(1)  # Add a delay to allow the text to be input

# Example usage
text_to_type = "สวัสดี, ยินดีที่ได้รู้จัก"
type_thai(text_to_type)สวัสดี, ยินดีที่ได้รู้จัก