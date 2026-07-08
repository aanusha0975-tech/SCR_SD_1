print("Temperature Converter")

temp = float(input("Enter temperature: "))

print("Choose input unit")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Fahrenheit =", (temp * 9/5) + 32)
    print("Kelvin =", temp + 273.15)

elif choice == 2:
    print("Celsius =", (temp - 32) * 5/9)
    print("Kelvin =", (temp - 32) * 5/9 + 273.15)

elif choice == 3:
    print("Celsius =", temp - 273.15)
    print("Fahrenheit =", (temp - 273.15) * 9/5 + 32)

else:
    print("Invalid choice")
