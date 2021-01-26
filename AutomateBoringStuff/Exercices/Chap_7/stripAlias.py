import re
def stripAlias(string, replace):
    if replace == "":
        stripReg = re.compile(r"(^\s*)|(\s*$)")
    else:
        stripReg = re.compile(replace)
    print(stripReg.sub("", string))

stripAlias("Bonjour ça va le jambon oui", "Bonjour")
stripAlias("Bonjour ça va le jambon oui","")
stripAlias("                Bonjour ça va le jambon oui             ","")
