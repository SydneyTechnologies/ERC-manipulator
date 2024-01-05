import cv2

# Load the video
cap = cv2.VideoCapture(0)

# Get the width and height of the video frames
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create a window to display the video
cv2.namedWindow('video', cv2.WINDOW_NORMAL)

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    if ret:
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply edge detection
        edges = cv2.Canny(gray, 100, 200)

        # Find the contours
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Find the biggest rectangle among the contours
        biggest_rectangle = None
        biggest_rectangle_area = 0
        for contour in contours:
            # Approximate the contour with a polygon
            approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

            # If the polygon has four sides, it's likely a rectangle
            if len(approx) == 4:
                # Calculate the area of the rectangle
                area = cv2.contourArea(approx)

                # If the area is bigger than the previous biggest rectangle, update it
                if area > biggest_rectangle_area:
                    biggest_rectangle = approx
                    biggest_rectangle_area = area

        if biggest_rectangle is not None:
            # Compute the center point of the biggest rectangle
            M = cv2.moments(biggest_rectangle)
            if M['m00'] != 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                # Draw the biggest rectangle on the frame
                cv2.drawContours(frame, [biggest_rectangle], 0, (0, 255, 0), 2)

                # Draw a circle at the center point of the biggest rectangle
                cv2.circle(frame, (cx, cy), 5, (0, 0, 255), -1)

                # Calculate the offset between the center of the image and the center of the biggest rectangle
                dx = cx - width/2
                dy = cy - height/2

                # Display the offset in the output window
                cv2.putText(frame, f'Offset: ({dx:.2f}, {dy:.2f})', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Display the frame in the output window
        cv2.imshow('video', frame)

        # Exit if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video and close the output window
cap.release()
cv2.destroyAllWindows()
