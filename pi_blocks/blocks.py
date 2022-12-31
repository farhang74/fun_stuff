import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import animation

def vs_after(m1,v1, m2,v2):
    v1_ = (((m1 - m2)/(m1+m2)) * v1) + (((2 * m2)/(m1+m2)) * v2)
    v2_ = (((m2 - m1)/(m1+m2)) * v2) + (((2 * m1)/(m1+m2)) * v1)
    return v1_, v2_ 

count = 0
v_bigger = -1
v_smaller = 0

m_bigger = 100
m_smaller = 1


# while True:
#     v_bigger, v_smaller = vs_after(m_bigger, v_bigger, m_smaller, v_smaller)
#     count += 1

#     if v_smaller < 0:
#         v_smaller = -v_smaller
#         count += 1

#     if v_bigger >= 0 and v_smaller >=0 and v_bigger > v_smaller:
#         print(count)
#         break



fig = plt.figure(figsize=(10,10))
plt.axis('equal')
ax = fig.add_subplot(111)
ax.set_aspect('equal', 'datalim')
ax.plot([0,0], [0, 1000])
ax.plot([0,1000], [0, 0])
fig.tight_layout()


bigger = patches.Rectangle((500, 0), 0, 0, fc='y')
smaller = patches.Rectangle((250, 0), 0, 0)

ax.add_patch(bigger)
ax.add_patch(smaller)

bigger.set_width(100)
bigger.set_height(100)
smaller.set_width(50)
smaller.set_height(50)


frames = 0
def animate(i):
    global v_bigger, v_smaller, count, frames
    if smaller.xy[0] <= bigger.xy[0] <= smaller.xy[0] + 50:
        count += 1
        # smaller.set_xy([bigger.xy[0] - 50, smaller.xy[1]])
        v_bigger, v_smaller = vs_after(m_bigger, v_bigger, m_smaller, v_smaller)

    if smaller.xy[0] <= 0:
        v_smaller = -v_smaller
        count +=1
    
    print(count)

    # if 

    bigger.set_xy([bigger.xy[0] + v_bigger, bigger.xy[1]])
    smaller.set_xy([smaller.xy[0] + v_smaller, smaller.xy[1]])

    frames += 1
    return bigger,smaller

anim = animation.FuncAnimation(fig, animate,
                               interval=1,
                               blit=True, 
                               save_count=1200)
plt.show()
# anim.save('test100.mp4')
