import sys

if len(sys.argv) < 2:
    print("usage: python temp.py <temperature_in_C>")
    sys.exit(1)

temp = float(sys.argv[1])

fahrenheit = (temp * 9/5) + 32
print("Temperature in Celsius:", temp)
print("Temperature in Fahrenheit:", fahrenheit)
