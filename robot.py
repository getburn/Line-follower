from gpiozero import Robot, LineSensor
from time import sleep
import signal, sys

robot = Robot(left=(7,8), right=(9,10))
left_sensor2 = LineSensor(17)
left_sensor1 = LineSensor(27)
right_sensor2 = LineSensor(23)
right_sensor1 = LineSensor(24)

def signal_nadler(sig, frame):
robot.stop()
sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

while True:
left_detect2 = int(left_sensor2.value)
left_detect1 = int(left_sensor1.value)
right_detect2 = int(right_sensor2.value)
right_detect1 = int(right_sensor1.value)
#print(left_detect2, left_detect1, right_detect2, right_detect1)

if left_detect2 == 1 and left_detect1 == 1 and right_detect1 == 1 and right_detect2 == 1:
robot.forward(0.3)
if left_detect2 == 1 and left_detect1 == 0 and right_detect1 == 1 and right_detect2 == 1:
robot.right(0.7)
robot.left(0.3)
if left_detect2 == 1 and left_detect1 == 1 and right_detect1 == 0 and right_detect2 == 1:
robot.right(0.3)
robot.left(0.7)
if left_detect2 == 0 and left_detect1 == 1 and right_detect1 == 1 and right_detect2 == 1:
robot.right(0.8)
robot.left(0.3)
if left_detect2 == 1 and left_detect1 == 1 and right_detect1 == 1 and right_detect2 == 0:
robot.right(0.3)
robot.left(0.8)
if left_detect2 == 1 and left_detect1 == 1 and right_detect1 == 0 and right_detect2 == 0:
robot.right(0)
robot.left(0.5)
if left_detect2 == 0 and left_detect1 == 0 and right_detect1 == 1 and right_detect2 == 1:
robot.right(0.5)
robot.left(0)