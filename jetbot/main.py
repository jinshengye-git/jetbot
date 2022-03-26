from robot import Robot
from time import time, sleep

if __name__=='__main__':
    try:
        robot=Robot()
        robot.right(100)
        now = time()
        #while time() - now < 7.5:
        #    sleep(1)

        robot.stop()
    except Exception as e:
        print(e)
