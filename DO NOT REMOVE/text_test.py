from pygame_functions import *

screenSize(800,800)

instructLabel = makeLabel("123", 40, 10, 10, "blue", "Agency FB", "yellow")
showLabel(instructLabel)

wordbox = makeTextBox(10, 80, 300, 0, "Enter text here", 20, 24)
showLabel(wordbox)
entry = textBoxInput(wordbox)
