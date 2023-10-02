import shutil
import pyautogui
from PIL import Image

import os
from pynput.keyboard import Key, Listener, Controller
import time
keyboard = Controller()

typed_characters = []

image_list = ["logIn.png", "sudParis.png", "casLogin.png", "pageDown.png", "lastStep.png"]

def backspace():
    keyboard.press(Key.backspace)
    keyboard.release(Key.backspace)

def printWord(word):
    for x in word:
        if x == "·":
            keyboard.type("\u00B7") #·
            #keyboard.type("\u30FB") #・ 
        else:
            keyboard.press(x)
            keyboard.release(x)

def login():
    start_time = time.time()
    while (time.time() - start_time) < 30:
        screenshot_folder = str(os.path.dirname(os.path.abspath(__file__)) + "/screenshots/")
        shutil.rmtree(screenshot_folder)
        os.mkdir(screenshot_folder)
        #print("haha")
        screenshot_path = str(screenshot_folder + "screen.png")
        screenshot = pyautogui.screenshot(screenshot_path)
        #print("hehe")
        for frame in image_list:
            match_location = pyautogui.locate(needleImage = str(os.path.dirname(os.path.abspath(__file__)) + "/cropped/" + frame), haystackImage = screenshot_path)


    # If the image is found, match_location will contain its coordinates
            if match_location is not None:
                if frame == "pageDown.png":
                    pyautogui.press('pagedown')
                else :
                    center_x = match_location.left + (match_location.width / 2)
                    center_y = match_location.top + (match_location.height / 2)
                    pyautogui.click(center_x, center_y)
        # Click on a specific location when the image is found

def on_press(key):
    global typed_characters
    try:
        # Check if the pressed key is a printable character
        char = key.char
        if char is not None:
            # Add the character to the typed_characters list
            typed_characters.append(char)
            # Keep only the last 100 characters
            typed_characters = typed_characters[-100:]
            # Check if the forbidden word is present
            typed_text = (''.join(typed_characters)).lower()
            #print (typed_text)
            if 'mood' in typed_text:
                login()
                # You can add your handling logic here (e.g., prevent further input)

    except AttributeError:
        # Handle special keys (e.g., Backspace)
        if key == key.backspace:
            # Remove the last character if Backspace is pressed
            if typed_characters:
                typed_characters.pop()

def on_release(key):
    pass

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

