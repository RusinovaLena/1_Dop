import numpy as np
import random as rand
import matplotlib.pyplot as plt
P = np.array([[0.1, 0.9],
              [0.4, 0.6]])
rand.seed(20)
state_sunny = 1
state_rainy = 2
t = 10
sunny_array = []
rainy_array = []
t_array = []


def theoretical_P(x):
    previous_P_sunny = 1
    previous_P_rainy = 0
    for x in range(x):
        next_P_sunny = P[0][0] * previous_P_sunny + P[1][0] * previous_P_rainy
        next_P_rainy = P[0][1] * previous_P_sunny + P[1][1] * previous_P_rainy
        previous_P_sunny = next_P_sunny
        previous_P_rainy = next_P_rainy
    return previous_P_sunny


def experiments(n):
    count = 10000
    countSunny = 0
    countRainy = 0
    for i in range(count):
        current = state_sunny

        for x in range(n):
            if (current == state_sunny):
                # генерируем случайное число от 0 до 1
                if (P[0][1] > rand.random()):
                    current = state_rainy
                else:
                    current = state_sunny
            else:
                if (P[1][0] > rand.random()):
                    current = state_sunny
                else:
                    current = state_rainy

        if (current == state_sunny):
            countSunny = countSunny + 1
        else:
            countRainy = countRainy + 1

    print("Count_sunny: ", countSunny)
    print("Count_rainy: ", countRainy)
    return countSunny / count

p_th_sunny_array = []
p_th_rainy_array = []
print("Result:")
for i in range(t):
    print(i)
    sunny = experiments(i)
    rainy = 1 - sunny
    print("P_sunny: ", sunny)
    print("P_rainy:", rainy)
    p_th_sunny = theoretical_P(i)
    print("P_th_sunny: ", p_th_sunny)
    p_th_rainy = 1 - p_th_sunny
    print("P_th_sunny: ", p_th_rainy)
    p_th_sunny_array.append(p_th_sunny)
    p_th_rainy_array.append(p_th_rainy)
    sunny_array.append(sunny)
    rainy_array.append(rainy)
    t_array.append(i)
f, ax = plt.subplots()
ax.plot(t_array, sunny_array, label ='sunny ')
ax.plot(t_array,  rainy_array,label ='rainy')
ax.plot(t_array, p_th_sunny_array, label ='sunny_th ')
ax.plot(t_array, p_th_rainy_array, label ='rainy_th')
ax.legend()
plt.show()



Result:
0
Count_sunny:  10000
Count_rainy:  0
P_sunny:  1.0
P_rainy: 0.0
P_th_sunny:  1
P_th_sunny:  0
1
Count_sunny:  991
Count_rainy:  9009
P_sunny:  0.0991
P_rainy: 0.9009
P_th_sunny:  0.1
P_th_sunny:  0.9
2
Count_sunny:  3676
Count_rainy:  6324
P_sunny:  0.3676
P_rainy: 0.6324000000000001
P_th_sunny:  0.37000000000000005
P_th_sunny:  0.6299999999999999
3
Count_sunny:  2956
Count_rainy:  7044
P_sunny:  0.2956
P_rainy: 0.7044
P_th_sunny:  0.28900000000000003
P_th_sunny:  0.711
4
Count_sunny:  3166
Count_rainy:  6834
P_sunny:  0.3166
P_rainy: 0.6834
P_th_sunny:  0.3133
P_th_sunny:  0.6867
5
Count_sunny:  3071
Count_rainy:  6929
P_sunny:  0.3071
P_rainy: 0.6929000000000001
P_th_sunny:  0.30601000000000006
P_th_sunny:  0.6939899999999999
6
Count_sunny:  3096
Count_rainy:  6904
P_sunny:  0.3096
P_rainy: 0.6904
P_th_sunny:  0.30819700000000005
P_th_sunny:  0.691803
7
Count_sunny:  3076
Count_rainy:  6924
P_sunny:  0.3076
P_rainy: 0.6924
P_th_sunny:  0.30754090000000006
P_th_sunny:  0.6924591
8
Count_sunny:  3086
Count_rainy:  6914
P_sunny:  0.3086
P_rainy: 0.6914
P_th_sunny:  0.3077377300000001
P_th_sunny:  0.6922622699999998
9
Count_sunny:  3094
Count_rainy:  6906
P_sunny:  0.3094
P_rainy: 0.6906
P_th_sunny:  0.30767868100000006
P_th_sunny:  0.6923213189999999


