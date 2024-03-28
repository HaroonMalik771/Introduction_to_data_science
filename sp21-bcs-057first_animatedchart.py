# Line Chart
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = [1, 2, 3]
y = [1, 2, 5]
y1 = [1, 3, 4]
x_i = np.linspace(1, 3, 500)
y_i = np.interp(x_i, x, y)
y1_i = np.interp(x_i, x, y1)

fig, ax = plt.subplots()
(line,) = ax.plot(x, y, color="red")
(line1,) = ax.plot(x, y1, color="blue")
text = ax.text(1, 1, "", color="green")
text1 = ax.text(1, 1, "", color="purple")


def update(i):
    line.set_data(
        x_i[:i], y_i[:i]
    )  # x[:i] and y[:i] is the subarray of x and y respectively
    line1.set_data(
        x_i[:i], y1_i[:i]
    )  # x[:i] and y[:i] is the subarray of x and y respectively
    text.set_position((x_i[i], y_i[i]))
    text.set_text(str(i))
    text1.set_position((x_i[i], y1_i[i]))
    text1.set_text(str(i))


anim = FuncAnimation(fig=fig, func=update, frames=1200, interval=2)

plt.show()
