import re
mo = (re.compile(r"(\d{3})-?(\d{3}-?\d{4})")).search('My number is 415-555-4242.')
try:
    print('Phone number found: ' + str(mo.group()))
except TypeError or AttributeError:
    print("Error LUL")

batRegex = re.compile(r'(Bat)(man|mobile|copter|bat)')
batlol = batRegex.search("Batmobile lost a wheel")
print(batlol.group())

batRegex = re.compile(r'Bat(wo)?man') #? veut dire "0 ou 1 itération du motif"
bat2Regex = re.compile(r"Bat(wo)*man")#* veut dire "[0:+infini[ itération du motif"
bat3Regex = re.compile(r"Bat(wo)+man")#+ veut dire "[1:+infini[ itération du motif"
mo1 = batRegex.search('The Adventures of Batman')
mo2 = batRegex.search("The Adventures of Batwoman")
mo3 = bat2Regex.search('The Adventures of Batwowowowoman')
print(mo1.group())
print(mo2.group())
print(mo3.group())

haRegex = re.compile(r'(Ha){3,5}') #Acolades pour {minimum, maximum} itérations du motif. GREEDY
mo1 = haRegex.search('HaHaHaHaHa')
print(mo1.group())

haRegex = re.compile(r"(Ha){3,5}?")# "?" après l'acolades indique une recherche "lazy",
#la plus petite expression matchant le motif sera renvoyée."""
mo2 = haRegex.search("HaHaHaHaHa")
print(mo2.group())

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # has no groups
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

vowelRegex = re.compile(r'[aeiouAEIOU]')#You can create your own character class by
#using brackets. No need to escape characters in it.
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

negVowelRegex = re.compile(r'[^aeiouAEIOU]')#"^" Crée une classe négative de caractères.
print(negVowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))

beginsWithHello = re.compile(r'^Hello') #"^" indique que le regex doit être au début de la str.
print(beginsWithHello.search('Hello, world!'))

helloRegex = re.compile(r"(H|h)ello!")
print(helloRegex.search("Hello!"))
print(helloRegex.search("hello!"))
print(helloRegex.search("ello!")==None)

atRegex = re.compile(r'.at') #"." = wildcard. Ne "remplace qu'un seul caractère. Ne marche pas
#pour "\n".
print(atRegex.findall('The cat in the hat sat on the flat mat.'))

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1)+" "+mo.group(2))

nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

#Utiliser "re.DOTALL" comme second argument de re.compile() permet de faire en sorte que "."
#match aussi les "\n".
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)

print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

#re.IGNORECASE pour ignorer sir le caractère est majuscule ou minuscule.
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())

#La méthode "sub()" permet de remplacer une regex par une str.
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

#On peut également introduire une partie du regex dans la substitution.
agentNamesRegex = re.compile(r'Agent (\w)(\w)\w*')
print(agentNamesRegex.sub(r'\2****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))

#l'argument re.VERBOSE permet d'intégrer des espaces ainsi que des commentaires dans la formule du regex,
#par exemple pour le rentre plus lisible.

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

#"|" (en l'occurence, le bitwise operator) permet d'utiliser plusieurs second arguments
#re.compile.
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
