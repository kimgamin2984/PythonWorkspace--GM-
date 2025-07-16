import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

m1, m2 = 2.0, 1.0
v1_init, v2_init = 2.0, -1.0
x1_init, x2_init = 1.0, 5.0
radius = 0.5
dt = 0.01
total_time = 5
n = int(total_time / dt)

x1 = np.zeros(n)
x2 = np.zeros(n)
v1 = np.zeros(n)
v2 = np.zeros(n)
p1 = np.zeros(n)
p2 = np.zeros(n)
F = np.zeros(n)

x1[0] = x1_init
x2[0] = x2_init
v1[0] = v1_init
v2[0] = v2_init
p1[0] = m1 * v1_init
p2[0] = m2 * v2_init

def handle_collision(v1, v2):
    new_v1 = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    new_v2 = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return new_v1, new_v2

for i in range(1, n):
    x1[i] = x1[i-1] + v1[i-1] * dt
    x2[i] = x2[i-1] + v2[i-1] * dt
    if abs(x1[i] - x2[i]) < radius + 0.1:
        v1[i], v2[i] = handle_collision(v1[i-1], v2[i-1])
        F[i] = abs(m1 * (v1[i] - v1[i-1])) / dt
    else:
        v1[i] = v1[i-1]
        v2[i] = v2[i-1]
        F[i] = 0
    p1[i] = m1 * v1[i]
    p2[i] = m2 * v2[i]

fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 1)
obj1, = ax.plot([], [], 'bo', markersize=20)
obj2, = ax.plot([], [], 'ro', markersize=20)

def animate(i):
    obj1.set_data([x1[i]], [0.5])
    obj2.set_data([x2[i]], [0.5])
    return obj1, obj2

ani = FuncAnimation(fig, animate, frames=n, interval=10, blit=True)
ani.save("collision_simulation.gif", writer=PillowWriter(fps=60))
plt.close()

time = np.linspace(0, total_time, n)

fig, axs = plt.subplots(3, 1, figsize=(8, 10))
axs[0].plot(time, p1, label='Momentum of Object 1')
axs[0].plot(time, p2, label='Momentum of Object 2')
axs[0].plot(time, p1 + p2, label='Total Momentum', linestyle='--')
axs[0].legend()
axs[0].set_title("Momentum Change")

axs[1].plot(time, F, color='green')
axs[1].set_title("Force over Time")

axs[2].plot(time, v1, label='Velocity 1')
axs[2].plot(time, v2, label='Velocity 2')
axs[2].legend()
axs[2].set_title("Velocity Change")

plt.tight_layout()
plt.savefig("collision_graph.jpeg", dpi=300)
plt.close()