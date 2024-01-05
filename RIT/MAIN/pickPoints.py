import cv2
import numpy as np
from getWorldCoordinates import getRealWorld
from EpsonController import sendToEpson
from TalkToServo import checkDistance
from take_picture import takePicture
import math
import time
# Load the image

sendToEpson(robot_z=850)
image = cv2.imread(takePicture())

# Create a copy of the image to draw circles on
image_copy = np.copy(image)

# Create an array to store the pixel coordinates
coordinates = []

# Define the mouse callback function


def pick_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        coordinates.append((x, y))
        new_x, new_y = getRealWorld(x, y)
        sendToEpson(x=new_x, y=new_y,)

        time.sleep(1)

        distance = checkDistance()
        if distance != 0 and distance != None:
            distance_z = 465
            if distance < 206: 
                if distance > 90:
                    distance_z =  465
                else: 
                    distance_z = (600 - distance) + 20
                
            
                print(distance_z)
            if distance_z < 465:
                distance_z = 465
        sendToEpson(new_x, new_y, robot_z = distance_z)


        time.sleep(1)

        sendToEpson(robot_z=850)








        

        print(f"Pixel coordinates: ({x}, {y})")

        font = cv2.FONT_HERSHEY_SIMPLEX
        color = (255, 0, 0)  # white color in BGR format

        # Get the size of the text
        text_size, _ = cv2.getTextSize(f"{new_x}{new_y}", font, 1, 2)

        # Draw a circle around the point on the image copy
        cv2.circle(image_copy, (x, y), 10, (255, 0, 0), 2)
        # Put the text on the image
        cv2.putText(
            image_copy, f"{math.ceil(new_x)}, {math.ceil(new_y)}", (x, y), font, 1, color, 2)

        # Display the image with circles
        cv2.imshow('image', image_copy)


# Display the image and wait for mouse clicks
cv2.imshow('image', image)
cv2.setMouseCallback('image', pick_points)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the points to a txt file
with open('picked_points.txt', 'w') as f:
    for coord in coordinates:
        f.write(f"{coord[0]} {coord[1]}\n")
