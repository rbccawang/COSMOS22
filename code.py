'''
Rotate Servo Back-and-Forth
Rebecca Wang
2022 July 13
'''

import adafruit_motor
import board
import time
import pwmio

# pwm variable
# dutycycle tells you if it's off or on (2^16; halfway is 2^15)
pwm = pwmio.PWMOut(board.A1, duty_cycle = 2**15, frequency = 50)

# servo variable
srv = adafruit_motor.servo.Servo(pwm)

# main loop
while True:
    aaa
