import pyperclip
import time
import pyautogui
from win32gui import GetWindowText, GetForegroundWindow
import pygame


def ring_buzzer():
    pygame.mixer.init()
    pygame.mixer.music.load("buzzer.mp3")
    pygame.mixer.music.play(-1)  # -1 means loop indefinitely

    while True:
        command = input("Type 'stop' to stop the buzzer: ")
        if command.lower() == 'stop':
            pygame.mixer.music.stop()
            break
    
def get_chrome_url():
    # Get the active indow
    window_title = GetWindowText(GetForegroundWindow())
    
    # Check if the active window is Chrome
    if 'Google Chrome' in window_title:
        # Focus on the address bar
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.5)
        
        # Copy the URL
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)
        
        # Get the URL from clipboard
        url = pyperclip.paste()
        return url
    else:
        return None

if __name__ == "__main__":
    while True:
        url = get_chrome_url()
        if url:
            if ("supplement" in url) or ("assignment-submission" in url):
                print(f"Current URL: {url}")
                print("\nReading/assigment detected!!\n")
                ring_buzzer()
        else:
            continue
        time.sleep(5)  # Wait for 5 seconds before checking again

