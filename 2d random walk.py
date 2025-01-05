import matplotlib.pyplot as plt
import numpy as np

# Function to simulate a 2D random walk
def random_walk_2d(steps):
    position = [0, 0]  # Starting position
    trajectory = [position.copy()]  # Include the initial position

    for _ in range(steps):
        step = np.random.choice([-1, 1])  # Step left (-1) or right (+1)
        direction = np.random.choice([0, 1])  # Step in x (0) or y (1)
        
        if direction == 0:  # Update x-coordinate
            position[0] += step
        else:  # Update y-coordinate
            position[1] += step
        
        trajectory.append(position.copy())  # Append current position snapshot

    return trajectory

if __name__ == "__main__":
    # Ask the user for the number of steps
    steps = int(input("Enter the number of steps for the random walk: "))
    trajectory = random_walk_2d(steps)

    # Unpack x and y coordinates for plotting
    x_coords = [pos[0] for pos in trajectory]
    y_coords = [pos[1] for pos in trajectory]

    # Plot the random walk
    plt.figure(figsize=(8, 6))
    plt.plot(x_coords, y_coords, '-o', label="Random Walk Path", markersize=4)
    plt.scatter(x_coords[0], y_coords[0], c='green', label="Start", zorder=5)  # Start point
    plt.scatter(x_coords[-1], y_coords[-1], c='red', label="End", zorder=5)  # End point
    plt.title("2D Random Walk", fontsize=14)
    plt.xlabel("X Direction", fontsize=12)
    plt.ylabel("Y Direction", fontsize=12)
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.axvline(0, color='gray', linestyle='--', linewidth=0.5)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(fontsize=10)
    plt.show()
