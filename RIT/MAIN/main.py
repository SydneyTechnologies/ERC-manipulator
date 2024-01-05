import cv2
import numpy as np
import DetectedObjects


img = cv2.imread("object1.jpg")

resized_img = cv2.resize(img, dsize=(0, 0), fx=0.3, fy=0.3)
cropped_img = resized_img[80:800, 220:1000]
cropped_img2 = img[40:800, 140:1000]


# cv2.imshow("Crop test", erosion)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
allObjects = DetectedObjects.DetectedObjects(cropped_img)

list_to_sort = allObjects.getContours()


def sortDetectedObjects(list_to_sort):
    return sorted(list_to_sort, key=lambda x: x.getPickScore((100, 250)))


sorted_list = sortDetectedObjects(list_to_sort)

for i in sorted_list:
    print(i.center_point, i.orientation)
