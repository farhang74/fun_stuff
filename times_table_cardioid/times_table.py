import matplotlib.pyplot as plt
import math
from matplotlib import animation

radius = 5
number_of_points = 200
center_point = [0,0]
times = 0
deg = 360 / number_of_points

def get_point_coordinates(degree, radius):
    x = radius*math.cos(math.radians(degree))
    y = radius*math.sin(math.radians(degree))
    return [x,y]

def get_circle_points(number_of_points):
    coordinates_dict = {}
    for i in range(number_of_points):
        degrees = deg * i
        xy = get_point_coordinates(degrees, radius)
        coordinates_dict[i] = xy
        # plt.scatter(xy[0], xy[1])
        # plt.text(xy[0], xy[1] + 0.1, i)
    return coordinates_dict

def plot_one_frame(times):
    fig, ax = plt.subplots(figsize=[5,5])

    for i in coordinates_dict:
        first_x = coordinates_dict[i][0]
        first_y = coordinates_dict[i][1]

        second_x =  get_point_coordinates(i * times * (360/number_of_points), radius)[0]
        second_y =  get_point_coordinates(i * times * (360/number_of_points), radius)[1]
        d = ax.plot([first_x, second_x], [first_y, second_y], color='purple', linewidth=0.3)
    ax.axis('off')
    plt.show()

coordinates_dict = get_circle_points(number_of_points)
# plot_one_frame(40)


fig, ax = plt.subplots(figsize=[5,5])
d = ax.scatter(center_point[0], center_point[1])

ax.axis('off')
ax.set_facecolor("#f8f8f8")

frames = 0
def animate(i):
    global ax, frames, times, fig
    ax.clear()
    ax.axis('off')

    times = times + 0.01

    for i in coordinates_dict:
        first_x = coordinates_dict[i][0]
        first_y = coordinates_dict[i][1]

        second_x =  get_point_coordinates(i * times * (360/number_of_points), radius)[0]
        second_y =  get_point_coordinates(i * times * (360/number_of_points), radius)[1]
        d = ax.plot([first_x, second_x], [first_y, second_y], color='purple', linewidth=0.2)

    frames += 1

anim = animation.FuncAnimation(fig, animate,
                               interval=1,
                            #    save_count=600,
                               )

plt.show()
# anim.save('times_table_cardioid.gif', fps=30)
