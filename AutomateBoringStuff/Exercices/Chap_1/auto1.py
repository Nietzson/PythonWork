from sys import exit
print("Hello world!")
name = input("What is your name?: ")
print(f"Nice to meet you, {name}.")
print(f"The lenght of your name is {len(name)} letters.")
age = input("What is your age?: ")
print(f"You will be {int(age)+1} years old next year.")

#Password program
def password():
    name= "Yoann"
    password="jambon123"

    while True:
        nameinput = input("Username?: ")
        if nameinput == name:
            while True:
                pwdinput = input("Password?: ")
                if pwdinput == password:
                    print("Access granted.")
                    return
                else:
                    print("Wrong password.")
        else:
            print("Incorrect Username.")

password()


