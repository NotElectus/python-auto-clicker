import pyautogui
import keyboard

# "0" starts the auto clicker.
# "1" stops the auto clicker.
# "3" stops the program.

# note: pressing 3 wll only stop the program if the clicker is not running.

print("started program:")

while True:
    if keyboard.is_pressed("1"):
        print("started clicker:")
        while True:
            pyautogui.click()
            if keyboard.is_pressed("2"):
                print("stopped clicker:")
                break
    if keyboard.is_pressed("3"):
        print("stopped program:")
        break
