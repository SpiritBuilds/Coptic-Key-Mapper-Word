from pynput import keyboard
from pynput.keyboard import Key, Controller
import time

kb = Controller()

#This Code should have an escape/pause functionallity
#It should aslo be compatible with the coptic font that Kero made (genius)
# I also realzed that it needs to account for Capitilzation

def on_press(key):
    try:
        if key.char == 'd':
            # Small delay to ensure 'd' isn't typed
            time.sleep(0.01)
            # Delete the 'd' that was just typed
            kb.press(Key.backspace)
            kb.release(Key.backspace)
            # Simulate Microsoft Symbol code for lower case delta 
            kb.press('0')
            kb.release('0')
            kb.press('3')
            kb.release('3')
            kb.press('B')
            kb.release('B')
            kb.press('4')
            kb.release('4')
            with kb.pressed(Key.alt):
                kb.press('x')
                kb.release('x')
            print("Macro triggered: Greek small letter delta")
        if key.char == 'a':
            #Pres and release necessary keys for the Microsoft word shortcut
            time.sleep(0.01)
            kb.press(Key.backspace)
            kb.release(Key.backspace)
            #with balh blah to activate the code in word
            kb.press('0')
            kb.release('0')
            kb.press('3')
            kb.release('3')
            kb.press('B')
            kb.release('B')
            kb.press('4')
            kb.release('4')
            with kb.pressed(Key.alt):
                kb.press('x')
                kb.release('x')
            #print that the macro was triggered
            print("Macro triggered: Coptic Nishti letter Alpha")
        
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        print("You pressed escape! we will pause the program")
        pause = input("Enter : ""resume"" to continue the program: ")
        if pause == "resume":
            return True
        else:
            return False
        # Stop listener
        #return False

print("Macro program started. Press 'q' to trigger Ctrl+V. Press 'esc' to exit.")
print("You can now switch to your Word document and start typing.")

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("Program terminated.")


# The program should be improved with switch case style structure to reduce the use of else statements, and clean the code execution time, strcture
# This makes the code more reader friendly
