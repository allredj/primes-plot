import numpy as np
import matplotlib.pyplot as plt

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Define a function to plot lines and points based on the new specifications
def plot_lines_and_points(start=1, end=101):
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()

    # Generate lines and points for each odd number from start to end
    for x in range(start, end + 1, 2):
        # if is_prime(x):# Loop prime numbers (not sure why i can't just use odd numbers)
            slope = 2 / x  # Calculate slope
            intercept = - x - 1  # Calculate intercept

            if (x == 15):
                slope = 6/5
                intercept = -24

            # Define the line function based on slope and intercept
            def line_func(x_value):
                return slope * x_value + intercept

            # Define x range for the line
            x_values = np.linspace(x, 300, 1000)
            y_values = line_func(x_values)

            # Plot the line
            ax.plot(x_values, y_values, label=f'Slope=2/{x}')

            # Plot points at x=3*2^n for n=0 to 4 as an example
            n_values = range(16)
            max_value = 300
            x_points = [x * 2 ** n for n in n_values if x * 2 ** n <= max_value]
            # x_points = [x * 2 ** n for n in n_values]
            y_points = [line_func(x_point) for x_point in x_points]
            ax.scatter(x_points, y_points, s=10)  # Plot points on the line

            # # Annotate points
            for (xp, yp) in zip(x_points, y_points):
                if (yp == 0 or xp == x_points[0]) :
                    ax.text(xp, yp, f'({xp},{yp:.2f})', fontsize=8)

    # Customize the plot
    ax.legend()
    ax.grid(True)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Abundance')

    # Show the plot
    plt.show()


# Call the function to plot the lines and points
plot_lines_and_points()