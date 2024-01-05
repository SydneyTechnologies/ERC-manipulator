import cv2
import numpy as np

# Load the image
img = cv2.imread("MAIN/test/Objects2.png")


# Set the coordinates for the section of the image you want to keep
x, y, w, h = 582, 136, 303, 303

# Crop the image
cropped_img = img[y:y+h, x:x+w]

# Create a black image with the same size as the original image
black_img = np.zeros_like(img)

# Replace the corresponding section of the black image with the cropped image
black_img[y:y+h, x:x+w] = cropped_img

# Display the resulting image
cv2.imshow("original", img)
cv2.imshow("Result", black_img)
cv2.imwrite(f"MAIN/test/selected.png", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


