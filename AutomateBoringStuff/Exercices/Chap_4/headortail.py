import random
numberOfStreaks = 0
iterations = 100
values = []
streak = 0
for experimentNumber in range(10000):
    #Code that creates a list of 100 "heads" or "tails" values.
    for i in range(iterations):
        values.append(random.randint(0,1))

    #Code that checks if there is a streak of 6 heads pr tails in a row.
for i in range(len(values)):
    if values[i]==values[i+1]==values[i+2]==values[i+3]==values[i+4]==values[i+5]:
        streak += 1



print("Chances of streak %s%%"%(streak/100))
