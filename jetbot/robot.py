from motor_driver import MotorDriver

class Robot():
    def __init__(self):
        self.__motor = MotorDriver()

    def forward(self, speed):
        self.__motor.motor_run(self.__motor.MOTOR_L.value,self.__motor.DIR_FORWARD.value,speed)
        self.__motor.motor_run(self.__motor.MOTOR_R.value,self.__motor.DIR_FORWARD.value,speed)

    def backward(self, speed):
        self.__motor.motor_run(self.__motor.MOTOR_L.value,self.__motor.DIR_BACKWARD.value,speed)
        self.__motor.motor_run(self.__motor.MOTOR_R.value,self.__motor.DIR_BACKWARD.value,speed)

    def stop(self):
        self.__motor.motor_stop(self.__motor.MOTOR_L.value)
        self.__motor.motor_stop(self.__motor.MOTOR_R.value)

    def left(self,speed):
        self.__motor.motor_run(self.__motor.MOTOR_L.value,self.__motor.DIR_SLOWLEFT.value,speed)
        self.__motor.motor_run(self.__motor.MOTOR_R.value,self.__motor.DIR_SLOWLEFT.value,speed/2)

    def right(self,speed):
        self.__motor.motor_run(self.__motor.MOTOR_R.value,self.__motor.DIR_SLOWRIGHT.value,speed)
        self.__motor.motor_run(self.__motor.MOTOR_L.value,self.__motor.DIR_SLOWRIGHT.value,speed/2)

