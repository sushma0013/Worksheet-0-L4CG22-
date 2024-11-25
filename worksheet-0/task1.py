cold = []
mild = []
comfortable = []
temperatures = [5, 12, 18, 9, 15, 20, 8, 14, 17, 19]


for temp in temperatures:
    if temp < 10:
        cold.append(temp)
    elif 10 <= temp <= 15:
        mild.append(temp)
    elif 15 < temp < 20:
        comfortable.append(temp)


print("Cold:", cold)
print("Mild:", mild)
print("Comfortable:", comfortable)

