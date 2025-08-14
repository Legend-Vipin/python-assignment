import turtle
import time

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Tower of Hanoi")

# Create turtle for drawing rods
rod_drawer = turtle.Turtle()
rod_drawer.speed(0)
rod_drawer.penup()
rod_drawer.goto(-150, -150)

# Draw the rods
for x in [-150, 0, 150]:
    rod_drawer.goto(x, -150)
    rod_drawer.pendown()
    rod_drawer.goto(x, 150)
    rod_drawer.penup()

# Create the disks
disk_turtles = []
disk_count = 3
disk_colors = ["red", "green", "blue"]
disk_width = [120, 100, 80]  # width of each disk

positions = [[], [], []]  # Represent rods

for i in range(disk_count):
    disk = turtle.Turtle()
    disk.shape("square")
    disk.shapesize(1, disk_width[i] / 20)
    disk.color(disk_colors[i])
    disk.penup()
    disk.goto(-150, -130 + i * 20)
    disk_turtles.append(disk)
    positions[0].append(i)

def move_disk(from_rod, to_rod):
    disk_index = positions[from_rod].pop()
    positions[to_rod].append(disk_index)

    disk = disk_turtles[disk_index]

    x_from = [-150, 0, 150][from_rod]
    x_to = [-150, 0, 150][to_rod]

    y = -130 + 20 * positions[to_rod].index(disk_index)

    # Animate movement
    disk.goto(x_from, 170)
    disk.goto(x_to, 170)
    disk.goto(x_to, y)

    time.sleep(0.5)

def hanoi(n, source, target, auxiliary):
    if n > 0:
        hanoi(n - 1, source, auxiliary, target)
        move_disk(source, target)
        hanoi(n - 1, auxiliary, target, source)

# Start the animation
hanoi(disk_count, 0, 2, 1)

# Keep the window open
screen.mainloop()
