import cv2
from EpsonController import sendToEpson, Home
from take_picture import takePicture
from DetectedObjects import DetectedObjects
from getWorldCoordinates import getRealWorld
from TalkToServo import talkToServo


SERVO_PORT = "/dev/cu.usbserial-1140"
# Open servo then go to the home point

Home()
talkToServo(14, SERVO_PORT)


# # Take picture 
# reference_path = takePicture()
# reference_image = cv2.imread(reference_path)


# # Get center points 
# # initialize detector
# Detector = DetectedObjects(reference_image)
# # gets the list objects in for of the object class
# Detector.getCenterPoints()

# object_list = Detector.getContours()

# # sort the objects by the pickscore
# sorted_list = Detector.sortDetectedObjects(object_list)

# # get first center point 
# target_object = sorted_list[0]
# targetX = target_object.center_point[0]
# targetY = target_object.center_point[1]
# targetU = target_object.orientation


# # convert to world coordinates
# worldX, worldY = getRealWorld(targetX, targetY)
# # go to the first center point
# sendToEpson(x=worldX, y=worldY, robot_z=600, robot_u=targetU)


# # open gripper 
# talkToServo(14, SERVO_PORT)


# # go down to default pick height 
# sendToEpson(worldX, worldY, 600)


# # close gripper 
# talkToServo(3, SERVO_PORT)


# # go to drop point 
# sendToEpson(x=-370, y=570, robot_z=850)


# # drop item in box
# talkToServo(14, SERVO_PORT)

# #go home
# Home()




