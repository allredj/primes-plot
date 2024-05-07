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

def sigma(n):
    factors = [1, n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sum(factors)

def slope_and_intercept(n):
    s = sigma(n)
    s2 = sigma(2 * n)
    slope = (s2 - 2 * n - s) / n # half_sigma(n) / n
    intercept = 2 * s - s2 # abundance(n) - half_sigma(n) = sigma(n) - 2n - (sigma(2n) -2n - sigma(n))
    return [slope, intercept]


# Define a function to plot lines and points based on the new specifications
def plot_lines_and_points(start=1, end=101):
    # Create a figure and axis for the plot
    fig, ax = plt.subplots()

    # Generate lines and points for each odd number from start to end
    for x in range(start, end + 1, 2):
        # if is_prime(x):# Loop prime numbers (not sure why i can't just use odd numbers)
            slope = 2 / x  # Calculate slope
            intercept = - x - 1  # Calculate intercept

            if x == 9: #9->-5, 18->3, 8/9, 8 is sum of half factors sigma(18) - 18 - sigma(9) = 8
                slope = 8/9
                intercept = - 5 - 8

            if x == 15: # 15-> -6, 30-> 12, 18/15
                slope = 18/15 # sigma(30) - 30 - sigma(15) = 18
                intercept = -24 # -6 - 15*18/15 = -6 - 18

            if x == 21: # 21 -> -10
                slope = 22/21 # sigma(42) - 42 - sigma(21) = 96-42-32=22
                intercept = -10 - 22

            if x == 25: # 25 -> -19
                slope = 12/25
                intercept = -19 - 12

            if x == 27: # 27 -> -14
                slope = 26/27 # sigma(54) - 54 - sigma(27) = 120-54-40=26
                intercept = -14 - 26

            if x == 33: # 33 -> -18
                slope = 30/33 # half_sigma(33) = 30
                intercept = -18 - 30

            if x == 35: # 35 -> -22
                slope = 26/35 # half_sigma(35) = 30
                intercept = -22 - 30

            if x == 39: # 39 -> -22
                slope = 34/39 # half_sigma(39) = 34
                intercept = -22 - 34

            if x == 45: # 45 -> -12
                slope = 66/45 # half_sigma(45) = 66
                intercept = -12 - 66

            if x == 49: # 49 -> -41
                slope = 16/49 # half_sigma(49) = 16
                intercept = -41 - 16

            if x == 51: # 51 -> -30
                slope = 42/51 # half_sigma(51) = 42
                intercept = -30 - 42

            if x == 55: # 55 -> -38
                slope = 34/55 # half_sigma(55) = 34
                intercept = -38 - 34

            if x == 57: # 57 -> -34 = sigma(i) - 2i
                [slope, intercept] = slope_and_intercept(x)

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

            # if x == 25:
            #     for (xp, yp) in zip(x_points, y_points):
            #         ax.text(xp, yp, f'({xp},{yp:.2f})', fontsize=8)

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
