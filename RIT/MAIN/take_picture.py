import cv2
# import keyboard

# camera = cv2.VideoCapture(0)
# count = 0

# while(True):
#     ret, frame = camera.read()
#     if ret:
#         cv2.imshow("table", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             count += 1
#             print("Take a picture")
#             cv2.imwrite(f"MAIN/test/Objects{count}.png", frame)
#             #break

#     # if keyboard.is_pressed("a"):
#     #     count += 1
#     #     print("Take a picture")
#     #     cv2.imwrite(f"{count}.png", frame)

# camera.release()
# # Destroy all the windows
# cv2.destroyAllWindows()


def takePicture(duration=5):
    camera = cv2.VideoCapture(0)
    image = None
    count_duration = 0
    while(count_duration < duration and image == None):
        open, frame = camera.read()
        if open: 
            count_duration+=1
            if count_duration > duration / 2:
                print("TAKING PICTURE")
                image = cv2.imwrite("MAIN/captures/pic.png", frame)
                print("PICTURE TAKEN")
                camera.release()
                cv2.destroyAllWindows()
                return "MAIN/captures/pic.png"




