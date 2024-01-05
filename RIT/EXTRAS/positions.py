distance = 50 
start_position = (-200, 380)
robot_points = []



for row in range(9):
    for col in range(9):
        new_pos = start_position[0] + row * distance, start_position[1] + col * distance
        robot_points.append(new_pos)

print(len(robot_points))
print(robot_points)