import re
dateReg = re.compile(r"([0-3]\d)/([0-1]?\d)/([1-2]\d{3})")
dateStr = "07/04/1995, 21/09/1992, 11/05/1961, 04/04/1964, 29/02/1995, 31/11/2000, 31/02/1945"
print(dateReg.findall(dateStr))
day = []
month = []
year = []
for date in dateReg.findall(dateStr):
    day.append(date[0])
    month.append(date[1])
    year.append(date[2])
for date in dateReg.findall(dateStr):
    if date[1] == "02":
        if date[0] in (1,28):
            print(str(date) + "is a valid date.")
        elif date[0]=="29" and (int(date[2])%4==0 or (int(date[2])%100==0 and int(date[2])%400==0)):
            print(str(date) + "is a valid date.")
    if date[1] in ["04","06","09","11"] and int(date[0]) in range(1,30):
            print(str(date) + "is a valid date.")
    elif date[1] in ["01","03","05","07","08","10","12"] and int(date[0]) in range(1,31):
        print(str(date) + "is a valid date.")
    else:
        print(str(date) + "is not a valid date.")


