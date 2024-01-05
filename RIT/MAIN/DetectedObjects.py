import cv2
import numpy as np
import math
from getWorldCoordinates import getPixel
# This class is resposinble for providing all data needed from the detected objects


parameters = cv2.aruco.DetectorParameters()
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50)
aruco_detector = cv2.aruco.ArucoDetector(aruco_dict, parameters)


class DetectedObjects():

    # Calibration constants
    pixel_cm = 1
    areaThresh = 850

    distanceThresh = 10

    # areaThresh = 20

    # Counterclockwise angle of objects from the x-axis
    orientation = 0

    def __init__(self, img) -> None:
        self.img = img
        self.gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_norm = cv2.normalize(
            self.gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        gray_norm2 = cv2.normalize(
            gray_norm, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        self.blur = cv2.GaussianBlur(gray_norm2, (1, 1), cv2.BORDER_DEFAULT)
        self.filter = cv2.bilateralFilter(self.blur, 10, 55, 55)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        erosion = cv2.erode(self.filter, kernel, iterations=7)
        dilation = cv2.dilate(erosion, kernel, iterations=7)
        self.edges = cv2.Canny(dilation, 50, 150)
        # Create a Mask with adaptive threshold
        mask = cv2.adaptiveThreshold(
            dilation, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 19, 5)
        self.contours = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        self.centers = []
        # self.mergeContours()
        self.objects = self.getContours()
        

    # def mergeContours(self):
    #     contours, _ = self.contours
    #     new_contours = list(contours)
    #     print(type(contours), type(contours[0]))
    #     merged_contours = []
    #     while len(new_contours) > 0:
    #         contour = new_contours.pop(0)
    #         for c in new_contours:
    #             dist = cv2.matchShapes(contour, c, cv2.CONTOURS_MATCH_I1,0)
    #             if dist < self.distanceThresh:
    #                 contour = np.concatenate((contour, c))
    #                 new_contours.remove()
    #             # if cv2.contourArea(c) > 130 and cv2.arcLength(c, False) < 2000 and cv2.arcLength(c, False) > 20:
    #             merged_contours.append(c)
    #         return merged_contours
    #     # self.contours = merged_contours
        

    def getContours(self):
        contours, _= self.contours
        objects = []
        index = 0
        px_cm = self.getDimensions()
        print("Pixel to cm ratio: ", px_cm)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > self.areaThresh:
                index += 1
                M = cv2.moments(cnt)
                # Check if the zeroth moment is not zero to prevent division be zero rule
                if M["m00"] != 0:
                    # Get the center x and center y of the objects in the contours
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                x, y, w, h = cv2.boundingRect(cnt)
                _, _, angle = cv2.minAreaRect(cnt)
                cv2.putText(self.img, str(int(w / px_cm)), (cx, cy),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 175, 255), 2)
                cv2.putText(self.img, str(int(h / px_cm)), (cx, cy + 20),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 175, 255), 2)
                if angle < 0:
                    angle = 90 + angle
                objects.append(PickableObjects(
                    (cx, cy), (int(w / px_cm), int(h / px_cm)), angle, (x, y)))
                # objects[f'object {index}'] = {"center_x": cx, "center_y": cy, "bound_x": x,
                #                               "bound_y": y, "pixel_w": int(w / px_cm), "pixel_h": int(h / px_cm), "angle": angle}
        return objects

    def getCenterPoints(self):
        contours, _ = self.contours
        # Draw the contours on the image
        cv2.drawContours(self.img, contours, -1, (0, 255, 0), 2)
        for cnt in contours:
            # epsilon = 0.05 * cv2.arcLength(cnt, True)
            # approx = cv2.approxPolyDP(cnt, epsilon, True)
            # Draw the contours on the image
            area = cv2.contourArea(cnt)
            if area > self.areaThresh:
                cv2.drawContours(self.img, cnt, -1, (0, 255, 0), 2)
                # calculate moment in contours
                M = cv2.moments(cnt)
                # Check if the zeroth moment is not zero to prevent division be zero rule
                if M["m00"] != 0:
                    # Get the center x and center y of the objects in the contours
                    cx = int(M['m10'] / M['m00'])
                    cy = int(M['m01'] / M['m00'])
                    self.centers.append([cx, cy])
                    cv2.putText(self.img, "0", (cx, cy),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                print("Centers: ", [cx, cy])
        self.centers = np.array(self.centers)
        cv2.imshow("Grey", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return self.centers

    def getBoundingBox(self):
        contours, _ = self.contours  # Access the contours from the state

        for cnt in contours:
            area = cv2.contourArea(cnt)  # calculate the contour areas
            if area > self.areaThresh:  # check if the contour area exceeds the required threshold
                # get the bounding box coordinates for the contours
                x, y, w, h = cv2.boundingRect(cnt)
                _, _, angle = cv2.minAreaRect(cnt)
                self.orientation = area
                # Draw the bounding box for each contour
                cv2.rectangle(self.img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(self.img, str(angle), (x, y),
                            cv2.FONT_HERSHEY_COMPLEX, 0.4, (0, 0, 255), 2)
        cv2.imshow("Grey", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return [x, y, w, h]

    def getDimensions(self):
        corners, _, _ = aruco_detector.detectMarkers(self.img)
        int_corners = np.int0(corners)
        cv2.polylines(self.img, int_corners, True, (0, 255, 0), 5)

        if corners:
            aruco_perimeter = cv2.arcLength(corners[0], True)

            self.pixel_cm = aruco_perimeter / 20
        else:
            self.pixel_cm = 1
        print("Gotten px to cm ratio")
        return self.pixel_cm

    def sortDetectedObjects(self, list_to_sort):
        sorted_list = sorted(list_to_sort, key=lambda x: x.getPickScore((0, 450)))
        accepted_list = []
        print(len(sorted_list))
        for item in sorted_list:
             if (item.center_point[0] > 450 and item.center_point[0] < 1470) and (item.center_point[1] > 70 and item.center_point[1] < 1050):
                 accepted_list.append(item)
        print(f"items detected: {len(accepted_list)}")
                 
        return accepted_list


class PickableObjects():
    # CONSTANT
    MAX_HEIGHT = 20
    HEIGHT_WEIGHT = 40

    MAX_WIDTH = 20
    WIDTH_WEIGHT = 40

    MAX_DISTANCE = 50
    DISTANCE_WEIGHT = 20

    def __init__(self, center_point, dimensions, orientation, boundaries) -> None:
        self.center_point = center_point
        self.dimensions = dimensions
        self.orientation = orientation
        self.boundaries = boundaries

    def getPickScore(self, mLoc):
        # mLoc refers to the position of the manipulator
        mLoc = getPixel(mLoc[0], mLoc[1])
        distance = math.dist(mLoc, self.center_point) / \
            self.MAX_DISTANCE * self.DISTANCE_WEIGHT
        width = (min(self.dimensions)/self.MAX_WIDTH) * self.WIDTH_WEIGHT
        _pickScore = distance + width
        return _pickScore
