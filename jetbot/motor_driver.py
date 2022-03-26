from PCA9685 import PCA9685
from enum import Enum
from time import time, sleep
class DIR(Enum):
    FORWARD =  'forward'    
    BACKWARD=  'backward'
    SPINLEFT=  'spinleft'
    SPINRIGHT= 'spinright'
    SLOWLEFT=  'slowleft'
    SLOWRIGHT= 'slowright'

class MOTOR(Enum):
    LEFT=  0
    RIGHT= 1
    MAX_VAL=100

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
        self.MOTOR_L=MOTOR.LEFT
        self.MOTOR_R=MOTOR.RIGHT
        self.MOTOR_MAX_VAL=MOTOR.MAX_VAL
        self.DIR_FORWARD=DIR.FORWARD
        self.DIR_BACKWARD=DIR.BACKWARD
        self.DIR_SPINLEFT=DIR.SPINLEFT
        self.DIR_SPINRIGHT=DIR.SPINRIGHT
        self.DIR_SLOWLEFT=DIR.SLOWLEFT
        self.DIR_SLOWRIGHT=DIR.SLOWRIGHT
    
    def motor_run(self, motor, index, speed):
        #  DC Motor :
        #  
        if speed > self.MOTOR_MAX_VAL.value:
            print('Speed should be 1 ~ 100')
            return
        if motor == self.MOTOR_L.value: #Left Motor
            pwm.setDutycycle(self.PWMA, speed)
            if index == self.DIR_FORWARD.value: # forward
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif index == self.DIR_BACKWARD.value : # backward
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            elif index == self.DIR_SPINLEFT.value: # spinleft
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif index == self.DIR_SPINRIGHT.value: # spinright
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            elif index == self.DIR_SLOWLEFT.value: # slowleft
                speed = speed * 0.8
                pwm.setDutycycle(self.PWMA, speed)
                pwm.setLevel(self.AIN1, 0)
                pwm.setLevel(self.AIN2, 1)
            elif index == self.DIR_SLOWRIGHT.value: # slowright
                speed = speed * 0.8
                pwm.setDutycycle(self.PWMA, speed)
                pwm.setLevel(self.AIN1, 1)
                pwm.setLevel(self.AIN2, 0)
            else:
                print('Wrong dir command')
                return                
        elif motor == self.MOTOR_R.value: #Right Motor
            pwm.setDutycycle(self.PWMB, speed)
            if index == self.DIR_FORWARD.value:
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif index == self.DIR_BACKWARD.value:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            elif index == self.DIR_SPINLEFT.value:
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif index == self.DIR_SPINRIGHT.value:
                pwm.setLevel(self.BIN1, 1)
                pwm.setLevel(self.BIN2, 0)
            elif index == self.DIR_SLOWLEFT.value:
                speed = speed * 0.8
                pwm.setDutycycle(self.PWMB, speed)
                pwm.setLevel(self.BIN1, 0)
                pwm.setLevel(self.BIN2, 1)
            elif index == self.DIR_SLOWRIGHT.value:
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

    def motor_stop(self, motor):
        if motor == self.MOTOR_L.value:
            pwm.setDutycycle(self.PWMA, pulse=0) #pulse 0 ~ 100
        elif motor == self.MOTOR_R.value:
            pwm.setDutycycle(self.PWMB, pulse=0)



#    def motor_slowright(self,speed):
#        self.motor_run(self.MOTOR_L.value,self.DIR_SLOWRIGHT.value,speed)
#        self.motor_run(self.MOTOR_R.value,self.DIR_SLOWRIGHT.value,speed/2)
#try:
#    Motor = MotorDriver()
    # control 2 motor
#    Motor.motor_run(Motor.MOTOR_L.value, Motor.DIR_SLOWRIGHT.value, 100) 
#    Motor.motor_run(Motor.MOTOR_R.value, Motor.DIR_SLOWRIGHT.value, 50)
    #Motor.motor_slowright(100)
#    now = time()
#    while time() - now < 6:
#        sleep(1);
#    Motor.motor_stop(1)
#    Motor.motor_stop(0)
#except IOError as e:
#    print(e)
    
#except KeyboardInterrupt:    
#    print("\r\nctrl + c:")
#    Motor.motor_stop(Motor.MOTOR_L.value)
#    Motor.motor_stop(Motor.MOTOR_R.value)
#    exit()


