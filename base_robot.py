from spike import PrimeHub, LightMatrix, Button, StatusLight, \
    ForceSensor, MotionSensor, Speaker, ColorSensor, App, \
    DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from spike.operator import greater_than, greater_than_or_equal_to, \
    less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
import sys
class BaseRobot():
    def __init__(self) -> None:
        self.hub = PrimeHub()
        self._version = "12/12/2022"
        self._leftDriveMotorPort = 'E'
        self._rightDriveMotorPort = 'A'
        self._leftAttachmentMotorPort = 'B'
        self._rightAttachmentMotorPort = 'D'
        self._colorSensorPort = 'F'
        self.driveMotors = MotorPair(self._leftDriveMotorPort,
                                     self._rightDriveMotorPort)
        self.debugMode = False
        self.colorSensor = ColorSensor(self._colorSensorPort)
        self.rightMedMotor = Motor(self._rightAttachmentMotorPort)
        self.leftMedMotor = Motor(self._leftAttachmentMotorPort)
        self._tireDiameter = 5.6  # CM
        self._tireCircum = self._tireDiameter * math.pi  # CM

        # Reset the yaw angle when the baseRobot is declared
        self.hub.motion_sensor.reset_yaw_angle()
    
    def AbortCheck(self):
        if(self.hub.right_button.is_pressed()):
            return()

    def GyroDrive(self, distance, maxspeed=50, heading=PrimeHub().motion_sensor.get_yaw_angle()):
        #Variables
        rotations = distance/self._tireCircum*360
        minspeed = 10
        currentspeed = 0
        proportionfactor = 1
        #Starts accelerating to the minimum speed
        for currentspeed in range(0,minspeed, 5):
            correction = heading-self.hub.motion_sensor.get_yaw_angle()
            self.driveMotors.start(correction*proportionfactor, currentspeed)
            wait_for_seconds()
            self.AbortCheck()
            
        #Cruises at maximum speed


    def GyroTurn(self, angle):
        turnspeed = 10
        
