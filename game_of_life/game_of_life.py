import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from matplotlib import animation

size = 200,200
grid = (np.random.random(size) > 0.9).astype(int)

kernel = np.array([[1,1,1],
                    [1,0,1],
                    [1,1,1]])

fig, ax = plt.subplots(figsize=[8,8])
# d = ax.scatter(center_point[0], center_point[1])
ax.axis('off')
ax.imshow(grid)


frames = 1
def animate(i):
    
    global ax, frames, grid, fig
    ax.clear()

    ax.axis('off')
    grid_new = signal.convolve2d(grid, kernel, mode='same', boundary='wrap')
    grid_new_copy = grid_new.copy()
    grid_new[grid_new_copy < 2] = 0

    grid_new[np.logical_and(grid == 1, grid_new_copy == 2)] = 1
    grid_new[np.logical_and(grid == 1, grid_new_copy == 3)] = 1

    grid_new[np.logical_and(grid == 0, grid_new_copy == 2)] = 0
    grid_new[np.logical_and(grid == 0, grid_new_copy == 3)] = 0
    
    grid_new[grid_new_copy > 3] = 0
    grid_new[np.logical_and(grid == 0, grid_new_copy == 3)] = 1

    ax.imshow(grid_new)
    grid = grid_new

    frames += 1

anim = animation.FuncAnimation(fig, animate,
                               interval=100,
                            #    save_count=600,
                               )

# anim.save('conway.gif')
plt.show()
