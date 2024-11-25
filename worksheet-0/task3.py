temperatures = [5, 12, 18, 9, 15, 20, 8, 14, 17, 19]

# Step 1: Create an empty list for Fahrenheit temperatures
temperatures_fahrenheit = []

# Step 2: Convert each temperature to Fahrenheit and store it in the new list
for temp in temperatures:
    fahrenheit = (temp * 9 / 5) + 32
    temperatures_fahrenheit.append(fahrenheit)

# Step 3: Print the converted Fahrenheit values
print("Temperatures in Fahrenheit:", temperatures_fahrenheit)