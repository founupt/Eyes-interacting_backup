Hi, thank you for your interest in my project. This is a system that interacts with the computer through eye movement, based on the Mediapipe model and PyAutoGUI. Due to limitations in device configuration and eye tracking, the system doesn't work perfectly as intended; it requires you to move your eyes to the area where you want to operate. I appreciate your understanding! :)

System Requirements
Hardware:
- Window
- An integrated webcam or an external camera (with a minimum resolution of 720p).
Software:
- Python 3.9 or higher.
- Lib: mediapipe, opencv-python, pyautogui, numpy, time.
=====================================
1) Run the login.py file.
- Enter user information:
- Fill in your name or personal information to start using the system.
2) Start tracking (please wait a moment).
The camera will automatically turn on to track your eyes. The screen will display the cursor position, gaze direction, and eye status (blinking or open).
3) Basic Operations:
  
- Blink your left eye to click the left mouse button (2times for double click or blink your eyes in 3s)
- Blink your right eye to click the right mouse button (DB click same as left eye)
- Look up/down( in the left side) to scroll the page.
- Close 2 eyes in 5s to automatic close
- Press Esc on the keyboard or close the application window.
