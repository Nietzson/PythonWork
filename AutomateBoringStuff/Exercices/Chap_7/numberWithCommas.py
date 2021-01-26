import re
def wata(string):
    wataRegex = re.compile(r"[A-Z]\w+ Watanabe")
    if wataRegex.search(string) != None:
        return True
    else:
        return False

print(wata("Haruto Watanabe"))
print(wata("Alice Watanabe"))
print(wata("RoboCop Watanabe"))
print(wata("haruto Watanabe"))
print(wata("Watanabe"))
print(wata("Mr. Watanabe"))
print(wata("Haruto watanabe"))

def three(string):
    tReg = re.compile(r"^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$", re.IGNORECASE)
    if tReg.search(string) != None:
        print(True)
    else:
        print(False)

three("Alice eats apples.")
three("Bob pets cats.")
three("Carol throws baseballs.")
three("Alice throws apples.")
three("BOB EATS CATS.")
three("RoboCop eats apples.")
three("ALICE THROWS FOOTBALLS.")
three("Carol eats 7 cats.")
