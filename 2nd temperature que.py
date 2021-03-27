#question no 2
#author - Nisha pagare
#date - 10-3-2021




temperature=int(input("Enter temperature in celcius:"))

if temperature < -273.15:
    print("Temperature is invalid because it is below absolute zero")
elif temperature == -273.15:
    print("Temperature is absolute 0")
elif temperature > -273.15 and temperature < 0:
    print("Temperature is below freezing")
elif temperature == 0:
    print("The temperature is at the freezing point")
elif temperature > 0 and temperature < 100:
    print("The temperature is in the normal range")
elif temperature == 100:
    print("The temperature is at the boiling point")
elif temperature > 100:
    print("The temperature is above the boiling point")
