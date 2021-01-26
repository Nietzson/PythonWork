import re
pswrd = ["123","123piou","123Piou","piouPiou","123PiouPiou"]
def password(pwd):
    pasReg1 = re.compile(r"[a-z]+")
    pasReg2 = re.compile(r"[A-Z]+")
    pasReg3 = re.compile(r"[0-9]+")
    pasReg4 = re.compile(r".{8,}")
    for pwd in pwd:
        test1 = pasReg1.search(pwd) == None
        test2 = pasReg2.search(pwd) == None
        test3 = pasReg3.search(pwd) == None
        test4 = pasReg4.search(pwd) == None
        if (test1 or test2 or test3 or test4) == True:
            print(pwd + " is not a strong enough password.")
        else:
            print(pwd + " is a strong enough password.")

password(pswrd)
