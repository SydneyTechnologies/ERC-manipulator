# First import opencv
import cv2

def takePicture(saveTo = "pictures"):
    # Start the camera
    cam = cv2.VideoCapture(0)
    # Take a picture
    ret, frame = cam.read()
    # Stop the camera
    cam.release()
    # Save the picture
    cv2.imwrite(f"{saveTo}/picture.png", frame)
    # Show the picture
    cv2.imshow("picture", frame)
    # Wait for the user to press a key
    cv2.waitKey(0)
    # Close the window
    cv2.destroyAllWindows()


takePicture()