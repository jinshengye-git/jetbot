#from robot import Robot
from time import time, sleep
from heartbeat import Heartbeat, signal_handler
from signal import SIGINT,signal

if __name__=='__main__':

    signal(SIGINT,signal_handler)
    heartbeat = Heartbeat()


    #try:
    #    robot=Robot()
    #    robot.right(100)
    #    now = time()
        #while time() - now < 7.5:
        #    sleep(1)

    #    robot.stop()
    #except Exception as e:
    #    print(e)

