import cv2
import numpy as np

def detectCircles(image):
    targetImage = cv2.imread(image)

    # convert image to grayscale
    gray = cv2.cvtColor(targetImage, cv2.COLOR_BGR2GRAY)

    # blur the image to remove noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use HoughCircles to detect circles
    circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 5, param1=100, param2=10, minRadius=4, maxRadius=10)

    # check if circles were found
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # loop over the (x, y) coordinates and radius of the circles
        for (x, y, r) in circles:
            # draw the circle in the output image
            cv2.circle(targetImage, (x, y), r, (0, 255, 0), 4)

        # show the output image
        outputImage = np.hstack([targetImage])
        cv2.imshow("Detected Circles", outputImage)

        key = cv2.waitKey(0)
        if key == ord('s'):
            cv2.imwrite('pictures/contours.png', outputImage)
            print("Image saved successfully!")
        cv2.destroyAllWindows()
    else:
        print("No circles were found.")



detectCircles("resources/calibration.png")