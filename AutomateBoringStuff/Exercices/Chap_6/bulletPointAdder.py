#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()
egg = []
bacon = text.split("\n")
for bacon in bacon:
    egg.append(bacon.rjust(len(bacon)+1,"*"))

jelly = "\n".join(egg)

pyperclip.copy(jelly)
