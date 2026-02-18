#Exercise 3: Lists
temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]
print("Temperature on Wednesday:", temperatures[2])

max_temp = 0
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp

min_temp = 1000
for temp in temperatures:
    if temp < min_temp:
        min_temp = temp

print("Max temp:", max_temp)
print("Min temp:", min_temp)

total = 0
for temp in temperatures:
    total += temp
average = round(total/len(temperatures), 1)

print("Average:", average)

days = 0
for temp in temperatures:
    if temp > 17:
        days += 1

print("Days above 17:", days)
temperatures.sort()
print("Sorted:", temperatures)


#another way to do thw min, max
#min = 1000
#max = 0
#total = 0
#days = []
#for i in range(len(temperatures)):
#   total += temperatures [i]
#   if temperatures[i] > max:
#       max = temperatures[i]
#   if temperatures[i] < min:
#       min = temperatures[i]
#   if temperatures[i] > 17:
#       days.append(temperatures[i])