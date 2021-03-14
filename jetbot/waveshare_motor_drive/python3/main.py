#!/usr/bin/python

from PCA9685 import PCA9685
import time
Dir = [
    'forward',
    'backward',
    'spinleft',
    'spinright',
    'slowleft',
    'slowright'
]
pwm = PCA9685(0x40, debug=True)
pwm.setPWMFreq(50)
class MotorDriver():
    def __init__(self):
        self.PWMA = 0
        self.AIN1 = 1
        self.AIN2 = 2
        self.PWMB = 5
        self.BIN1 = 3
        self.BIN2 = 4

    def MotorRun(self, motor, index, speed):
        #  DC Motor :
        #  
        if speed > 100:
            return
        if(motor == 0): #Left Motor
            pwm.setDutycycle(self.PWMA, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif (index == Dir[1]):
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            elif (index == Dir[2]):
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif (index == Dir[3]):
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            elif (index == Dir[4]):

            else:
                pass
                
        else: #Right Motor
            pwm.setDutycycle(self.PWMB, speed)
            if(index == Dir[0]):
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif (index == Dir[1]):
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            elif (index == Dir[2]):
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif (index == Dir[3]):
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            elif (index == Dir[4]):
            else:
                pass

    def MotorStop(self, motor):
        if (motor == 0):
            pwm.setDutycycle(self.PWMA, 0)
        else:
            pwm.setDutycycle(self.PWMB, 0)


try:
    Motor = MotorDriver()
    # control 2 motor
    Motor.MotorRun(0, 'spinright', 100) 
    Motor.MotorRun(1, 'spinright', 100)
    #print("sssssssss1")
    while(1):
        time.sleep(1);

except IOError as e:
    print(e)
    
except KeyboardInterrupt:    
    print("\r\nctrl + c:")
    Motor.MotorRun(0, 'forward', 0)
    Motor.MotorRun(1, 'backward', 0)
    exit()

