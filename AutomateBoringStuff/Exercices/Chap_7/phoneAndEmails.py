#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# TODO: Create email regex.
mailRegex = re.compile(r"""(
(\w*)                                #Begining of the mail address
((-|\.)?(\w*))*?                     #Potential extension on the name of the address
(@)                                  #"@"
(\w*)                                #"gmail", "free" etc.
(\.)(\w*)                            #".com", ".uk" etc.
)""", re.VERBOSE)

# TODO: Find matches in clipboard text.
matches = []
text = str(pyperclip.paste())
mailResult = mailRegex.findall(text)
for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8]!= "":
        phoneNum += "x"+groups[8]
    matches.append(phoneNum)

for groups in mailRegex.findall(text):
    matches.append(groups[0])

# TODO: Copy results to the clipboard.
mailList = "list of email address:\n"
phoneList = "List of phone numbers:\n"
for item in matches:
    if "@" in item:
        mailList += item + "\n"
    else:
        phoneList += item + "\n"
List = mailList + "\n" + phoneList
if List == "":
    List = "No email address nor phone numbers found in the text."
pyperclip.copy(List)
print("Copied to clipboard.")
