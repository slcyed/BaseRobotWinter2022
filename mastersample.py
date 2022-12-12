# LEGO type:standard slot:5 autostart

from spike import PrimeHub, LightMatrix, Button, StatusLight, \
    ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import base_robot

br = base_robot.BaseRobot()

def mission1():
    br.hub.light_matrix.show_image("CHESSBOARD")
def mission2():
    br.hub.light_matrix.show_image("CHESSBOARD")
def mission3():
    br.hub.light_matrix.show_image("CHESSBOARD")

#Pre run gyro check
currentgyro = br.hub.motion_sensor.get_yaw_angle()
position = 1
while(br.hub.motion_sensor==currentgyro):
    br.hub.light_matrix.show_image("CLOCK"+str(position))
    position = position + 1
    wait_for_seconds(0.3)

#Master Loop
validColorList = ['azure','blue','cyan','green','orange','pink','red',\
    'violet','yellow','white']
while(True):
    while(True):
        
        color = br.colorSensor.get_color()
        if(color in validColorList):
            br.hub.status_light.on(color)
            br.hub.light_matrix.show_image("YES")
        else:
            br.hub.status_light.off()
            br.hub.light_matrix.show_image("CONFUSED")
        if(br.hub.left_button.is_pressed):
                print("work")
                break
    if(color=="red"):
        mission1
    if(color=="blue"):
        mission1
    if(color=="white"):
        mission1