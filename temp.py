import sys

temp = float(input("Enter the temperature in °C: "))

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")
