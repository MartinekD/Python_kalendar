import calendar
year = int(input("Zadej rok: "))
month = int(input("Zadej měsíc: "))
x = calendar.month(year, month)
print(x)