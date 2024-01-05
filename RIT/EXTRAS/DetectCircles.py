import cv2
import numpy as np

# Load the image
image = cv2.imread('1.png')

# Convert to grayscale and apply blur
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect circles using the Hough circle transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Draw dots around the centers of the detected circles
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(image, (x, y), 2, (0, 255, 0), 2)
        print(f"Coordinates x: {x}, y: {y}")

# Display the image with circles and dots
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the center coordinates to a txt file
if circles is not None:
    with open('circle_centers.txt', 'w') as f:
        for (x, y, r) in circles:
            f.write(f"{x} {y}\n")
