
temperatures = [15, 14, 13, 12, 11, 10, 9, 8, 22, 25, 28, 30, 33, 35, 37, 36, 29, 27, 25, 23, 20, 18, 17, 16]


night_temps = []
evening_temps = []
day_temps = []


for i, temp in enumerate(temperatures):
    if 0 <= i < 8:  # Night: 00-08
        night_temps.append(temp)
    elif 8 <= i < 16:  # Evening: 08-16
        evening_temps.append(temp)
    elif 16 <= i < 24:  # Day: 16-24
        day_temps.append(temp)


if day_temps:
    avg_day_temp = sum(day_temps) / len(day_temps)
    print(f"Average Day-Time Temperature: {avg_day_temp:.2f}°C")
else:
    print("No day-time temperature data available.")


    
    

