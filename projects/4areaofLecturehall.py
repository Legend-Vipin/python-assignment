def calculate_painting_cost(length, width, height, cost_per_liter, num_windows, num_doors, window_area, door_area):
    # Calculate the total surface area to be painted (walls and ceiling)
    wall_area = 2 * (length + width) * height  # Surface area of the walls
    ceiling_area = length * width  # Area of the ceiling
    total_area = wall_area + ceiling_area  # Total area to be painted

    # Subtract areas of windows and doors
    total_window_area = num_windows * window_area
    total_door_area = num_doors * door_area
    total_area -= (total_window_area + total_door_area)  # Remove window and door areas

    # Define the coverage area of 1 liter of paint (assuming coverage is 10 square meters per liter)
    coverage_per_liter = 10  # This can vary, but we assume 10m² per liter as an example

    # Calculate the amount of paint needed
    liters_needed = total_area / coverage_per_liter

    # Calculate the total cost
    total_cost = liters_needed * cost_per_liter
    return total_cost


# Example usage:
length = float(input("Enter the length of the hall (in meters): "))
width = float(input("Enter the width of the hall (in meters): "))
height = float(input("Enter the height of the hall (in meters): "))
cost_per_liter = 333  # Given cost per liter of paint

# Input for windows and doors
num_windows = int(input("Enter the number of windows: "))
window_area = float(input("Enter the area of one window (in square meters): "))
num_doors = int(input("Enter the number of doors: "))
door_area = float(input("Enter the area of one door (in square meters): "))

# Calculate the painting cost
cost = calculate_painting_cost(length, width, height, cost_per_liter, num_windows, num_doors, window_area, door_area)

print(f"The total cost of painting the interior of the hall is: {cost:.2f} units.")
