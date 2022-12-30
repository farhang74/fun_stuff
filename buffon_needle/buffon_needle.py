import random
import numpy as np
import matplotlib.pyplot as plt

number_of_needls = 500
plot_flag = True

line_interval = 2
radius = 1
count = 0
int_list = []
needles = []


int_list = list(range(0,11,line_interval))

for num in range(number_of_needls):
    x0 = random.random()*10
    y0 = random.random()*10

    random_angle = random.random()*360

    x1 = x0 + radius * np.cos(np.deg2rad(random_angle))
    y1 = y0 + radius * np.sin(np.deg2rad(random_angle))
    p0 = [x0, y0]
    p1 = [x1, y1]

    needles.append([[x0,x1], [y0, y1]])
    for i in int_list:
        if p0[0] <= i <= p1[0] or p1[0] <= i <= p0[0]:
            count +=1


if plot_flag:
    fig = plt.figure(figsize=(10,10))
    for interval in int_list:
        d =  plt.plot([interval,interval],[0,10], color='red')

    for needle in needles:
        d = plt.plot(needle[0], needle[1])

    plt.xlim(-1,11)
    plt.ylim(-1,11)
    plt.title(f'number of needles: {number_of_needls} \n number of intersects: {count} \n estimated pi: {number_of_needls/count}')
    plt.show()


print(number_of_needls/count)
# 3.14159265359