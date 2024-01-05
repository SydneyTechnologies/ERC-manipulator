from EpsonController import sendToEpson


while(True):
    x = eval(input("enter x value: "))
    y = eval(input("enter y value: "))
    z = eval(input("enter z value: "))
    u = eval(input("enter u value: "))

    
    sendToEpson(x=x, y=y, robot_z=z, robot_u=u)