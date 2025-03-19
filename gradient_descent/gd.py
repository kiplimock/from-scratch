import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output

def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5

def calculate_gradient(x, y):
    return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * y) * np.sin(5 * y)


x = np.arange(-1, 1, 0.05)
y = np.arange(-1, 1, 0.05)

X, Y = np.meshgrid(x, y)
Z = z_function(X, Y)

current_pos1 = (0.7, 0.4, z_function(0.7, 0.4))
current_pos2 = (0.3, 0.8, z_function(0.3, 0.8))
current_pos3 = (-0.5, 0.5, z_function(-0.5, 0.5))
learning_rate = 0.01

ax = plt.subplot(projection='3d', computed_zorder=False)

for _ in range(1000):
    # clear the output  
    # clear_output(wait=True)

    # update X and Y
    X_derivative, Y_derivative = calculate_gradient(current_pos1[0], current_pos1[1])
    new_X = current_pos1[0] - learning_rate * X_derivative
    new_Y = current_pos1[1] - learning_rate * Y_derivative
    current_pos1 = (new_X, new_Y, z_function(new_X, new_Y))

    # update X and Y
    X_derivative, Y_derivative = calculate_gradient(current_pos2[0], current_pos2[1])
    new_X = current_pos2[0] - learning_rate * X_derivative
    new_Y = current_pos2[1] - learning_rate * Y_derivative
    current_pos2 = (new_X, new_Y, z_function(new_X, new_Y))

    # update X and Y
    X_derivative, Y_derivative = calculate_gradient(current_pos3[0], current_pos3[1])
    new_X = current_pos3[0] - learning_rate * X_derivative
    new_Y = current_pos3[1] - learning_rate * Y_derivative
    current_pos3 = (new_X, new_Y, z_function(new_X, new_Y))


    # display the plot
    ax.plot_surface(X, Y, Z, cmap='viridis', zorder=0)
    ax.scatter(current_pos1[0], current_pos1[1], current_pos1[2], color='magenta', zorder=1)
    ax.scatter(current_pos2[0], current_pos2[1], current_pos2[2], color='green', zorder=1)
    ax.scatter(current_pos3[0], current_pos3[1], current_pos3[2], color='red', zorder=1)
    plt.pause(0.001)
    ax.clear()