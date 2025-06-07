import time
import pyautogui
import pyperclip

# Attempt to import pygetwindow for window detection
try:
    import pygetwindow as gw
    USE_WINDOW_DETECTION = True
except ImportError:
    USE_WINDOW_DETECTION = False

# Configuration
delay_before_start = 5           # seconds to give time to focus Zoom window
poll_check_interval = 10          # seconds between each poll check
tabs_to_radio = 3                # number of Tab presses to reach the first radio option
tabs_to_submit = 2               # number of Tab presses to reach the Submit button
heading_keyword = 'attendance'   # text expected in the poll heading


def focus_poll_window() -> bool:
    """
    Finds and focuses the Zoom poll window by title 'Polls/Quizzes'.
    Returns True if successful.
    """
    if not USE_WINDOW_DETECTION:
        return False
    try:
        windows = gw.getWindowsWithTitle('Polls/Quizzes')
        if windows:
            win = windows[0]
            win.activate()
            time.sleep(0.5)
            return True
    except Exception:
        pass
    return False


def verify_poll_heading() -> bool:
    """Copy the heading text and verify it contains ``heading_keyword``."""
    try:
        # The first Tab focuses the poll heading
        pyautogui.press('tab')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)
        text = pyperclip.paste().lower()
        pyautogui.hotkey('shift', 'tab')  # return focus
        return heading_keyword.lower() in text
    except Exception:
        return False


def keyboard_navigation() -> bool:
    """
    Uses keyboard navigation to answer the poll:
    1) Tab to the first radio option
    2) Press Down to select the radio (Yes)
    3) Press Enter to choose the first option
    4) Tab to Submit
    5) Press Enter to submit the poll
    Only runs when poll window is focused.
    """
    if not focus_poll_window():
        return False
    if not verify_poll_heading():
        print("Poll does not appear to be attendance; skipping")
        return False
    try:
        # Move focus to the 'Yes' radio option
        pyautogui.press('tab', presses=tabs_to_radio, interval=0.3)
        # Select the radio option using Down arrow
        pyautogui.press('down')
        # Confirm the selection
        pyautogui.press('enter')
        # Move focus to the Submit button
        pyautogui.press('tab', presses=tabs_to_submit, interval=0.4)
        # Submit the poll
        pyautogui.press('enter')
        print("Poll answered successfully")
        return True
    except Exception:
        return False


def main():
    print(f"Starting in {delay_before_start} seconds. Please focus your Zoom poll window...")
    time.sleep(delay_before_start)
    print(f"Checking for polls every {poll_check_interval} seconds. Press Ctrl+C to stop.")

    try:
        while True:
            keyboard_navigation()
            time.sleep(poll_check_interval)
    except KeyboardInterrupt:
        print("Automation stopped by user.")
    print("Exiting script.")

if __name__ == '__main__':
    main()
