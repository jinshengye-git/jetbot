#!/usr/bin/python

from PCA9685 import PCA9685
from time import time, sleep
from enum import Enum

BRAKE_SMOOTHER = [0.]
class DIR(Enum):
    FORWARD :  'forward'    
    BACKWARD:  'backward'
    SPINLEFT:  'spinleft'
    SPINRIGHT: 'spinright'
    SLOWLEFT:  'slowleft'
    SLOWRIGHT: 'slowright'
class MOTOR(Enum):
    LEFT:  0
    RIGHT: 1

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)
class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.BIN1 = 3
        self.BIN2 = 4
        self.PWMB = 5

    def MotorRun(self, motor, index, speed):
        #  DC Motor :
        #  
        if speed > 100:
            print('Speed should be 1 ~ 100')
            return
        if motor == MOTOR.LEFT: #Left Motor
            pwm.setDutycycle(self.PWMA, speed)
            if index == DIR.FORWARD: # forward
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif index == DIR.BACKWARD : # backward
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            elif index == DIR.SPINLEFT: # spinleft
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif index == DIR.SPINRIGHT: # spinright
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            elif index == DIR.SLOWLEFT: # slowleft
                speed = speed * 0.8
                pwm.setDutycycle(self.PWMA, speed)
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif index == DIR.SLOWRIGHT: # slowright
                speed = speed * 0.8
                pwm.setDutycycle(self.PWMA, speed)
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            else:
                print('Wrong dir command')
                return                
        elif motor == MOTOR.RIGHT: #Right Motor
            pwm.setDutycycle(self.PWMB, speed)
            if index == DIR.FORWARD:
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif index == DIR.BACKWARD:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            elif index == DIR.SPINLEFT:
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif index == DIR.SPINRIGHT:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            elif index == DIR.SLOWLEFT:
                speed = speed * 0.8
                pwm.setDutycycle(self.PWMB, speed)
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif index == DIR.SLOWRIGHT:
                speed = speed * 0.8
                pwm.setDutycycle(self.PWMB, speed)
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            else:
                print('Wrong dir command')
                return
        else:
            print('Wrong motor value')
            return

    def MotorStop(self, motor):
        if motor == MOTOR.LEFT:
            pwm.setDutycycle(self.PWMA, pulse=0) #pulse 0 ~ 100
        elif motor == MOTOR.RIGHT:
            pwm.setDutycycle(self.PWMB, pulse=0)

    def MotorSmootherStop(self, motor):
        if motor == MOTOR.LEFT:
            pwm.setDutycycle(self.PWMA, pulse=70)
            pwm.setDutycycle(self.PWMA, pulse=40)
            pwm.setDutycycle(self.PWMA, pulse=10)
            pwm.setDutycycle(self.PWMA, pulse=0)
        elif motor == MOTOR.RIGHT:
            pwm.setDutycycle(self.PWMB, pulse=70)
            pwm.setDutycycle(self.PWMB, pulse=40)
            pwm.setDutycycle(self.PWMB, pulse=10)
            pwm.setDutycycle(self.PWMB, pulse=0)


"""
try:
    Motor = MotorDriver()
    # control 2 motor
    Motor.MotorRun(0, 'slowright', 100) 
    Motor.MotorRun(1, 'slowright', 50)

    while(1):
        sleep(1);

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("\r\nctrl + c:")
    Motor.MotorRun(0, 'forward', 0)
    Motor.MotorRun(1, 'backward', 0)
    exit()
"""

