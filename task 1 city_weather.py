import numpy as np

temps = np.array([
    [30, 32, 31, 29, 28, 27, 26],   # City A
    [22, 21, 23, 24, 25, 26, 24],   # City B
    [15, 17, 16, 18, 19, 20, 21]    # City C
])

max_temp_A = temps[0].max()
print("City A is max temp:", max_temp_A)

daily_max = temps.max(axis=0)  
overall_max_day = daily_max.argmax()  
print("Hot day (0 Meins first day):", overall_max_day)

avg_A = temps[0].mean()  
avg_B = temps[1].mean()

if avg_A > avg_B:
    print("city A is very hot (avg temp is high)")
else:
    print("city B iv very warm (avg temp is high)")