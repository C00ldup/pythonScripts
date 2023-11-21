# https://nitratine.net/blog/post/how-to-use-pynputs-mouse-and-keyboard-listener-at-the-same-time/

from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller

mouseController = Controller()
keyboardController = Controller()

print(mouseController.position)
mouseController.move(5, 5)