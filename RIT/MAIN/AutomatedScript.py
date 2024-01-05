import cv2
import numpy as np
import DetectedObjects
# from EpsonController import sendToEpson, DROP_POINT
from getWorldCoordinates import getRealWorld

home = "0 "

reference_image = cv2.imread("MAIN/captures/pic.png")
# resized_img = cv2.resize(reference_image, (0, 0), fx=0.4, fy=0.4)
# cropped_img2 = reference_image[80:1300, 140:1000]
# cv2.imshow("frame", cropped_img2)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
center_points = []

src_points = np.float32([(412, 14), (1663, 14), (1663, 1059), (412, 1059)])
dst_points = np.float32([(400, 10), (1623, 10), (1623, 1039), (400, 1039)])

M = cv2.getPerspectiveTransform(src_points, dst_points)

# output = cv2.warpPerspective(reference_image, M, (1700, 1200))


detector = DetectedObjects.DetectedObjects(reference_image)
detector.getCenterPoints()
object_list = detector.getContours()
# sorted_list = detector.sortDetectedObjects(object_list)


for item in object_list:
    if (item.center_point[0] > 230 and item.center_point[0] < 1350) and (item.center_point[1] > 70 and item.center_point[1] < 1050):
        center_points.append(item.center_point)

# Save the points to a txt file
# with open('MAIN/picked_points.txt', 'w') as f:
#     count = 0
#     for item in object_list:
#         count += 1
#         if count < (len(object_list) - 1):
#             f.write(f"{item.center_point[0]} {item.center_point[1]}\n")

print("items detected: ", len(center_points))

# for center in center_points:
#     new_x, new_y = getRealWorld(center[0], center[1])
#     print(f"{center} to real world: {new_x}, {new_y}")
#     sendToEpson(x= new_x, y= new_y, robot_z=600, robot_u=0)
#     sendToEpson()
#     sendToEpson(-400, 500, 800, 0) # DROP POINT
#     print(f"Destination Reached: {new_x}, {new_y}")
