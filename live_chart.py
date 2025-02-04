import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# Create a figure and an axis
fig, ax = plt.subplots()

# Initialize x and y data
x_data, y_data = [], []

# Define the update function for the chart
def update(i):
    # Simulate receiving new data
    x_data.append(i)
    y_data.append(random.randint(0, 100))  # Random data for demonstration

    # Update the plot with new data
    ax.clear()
    ax.plot(x_data, y_data)

    # Set labels and title
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.set_title('Real-Time Data Update')

    # Improve layout and refresh the plot
    plt.tight_layout()

# Use FuncAnimation to animate the plot
ani = animation.FuncAnimation(fig, update, interval=1000)  # Update every 1000ms (1 second)

# Show the live plot
plt.show()
